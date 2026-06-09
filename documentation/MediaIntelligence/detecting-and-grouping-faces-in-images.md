# Detecting and grouping faces in images

**Framework**: Media Intelligence

Organize photos by person using on-device face detection.

#### Overview

Apps that work with photo collections often need to identify who appears in each image and group photos by person. To simplify this task, [`FaceGroupAnalyzer`](facegroupanalyzer.md) provides on-device face detection along with automatic grouping by person. Because all processing happens on device, face data remains private and no network connection is required.

The analyzer stores all face data in a working directory you provide. The framework exclusively manages the contents of this directory, so your app interacts with the stored data only through the [`FaceGroupAnalyzer`](facegroupanalyzer.md) API. This data persists between app launches, so the analyzer resumes where it left off. The typical workflow has three phases: add images to detect faces, group the detected faces by person, and retrieve the results.

#### Create a Face Group Analyzer

To set up the analyzer, create a writable directory that the analyzer uses to store its face data and metadata, then pass it to [`init(workingDirectory:)`](facegroupanalyzer/init(workingdirectory:).md):

```swift
let workingDirectory = URL.documentsDirectory
    .appending(path: "FaceGroupData", directoryHint: .isDirectory)

// Create the directory if it doesn't already exist.
try FileManager.default.createDirectory(
    at: workingDirectory, 
    withIntermediateDirectories: true
)

let analyzer = try FaceGroupAnalyzer(workingDirectory: workingDirectory)
```

After initializing the analyzer, it’s ready to accept images. If the directory already contains data from a previous session, the analyzer loads it automatically.

#### Add Image Assets

Create [`MediaIntelligenceImageAsset`](mediaintelligenceimageasset.md) values to identify each image you want the analyzer to process. Each asset takes a unique identifier you assign and a [`MediaIntelligenceImageAsset.Kind`](mediaintelligenceimageasset/kind-swift.enum.md) value that tells the framework how to access the image data. Use the same identifier consistently for each image, because the framework uses it to match new submissions against existing data.

Call [`insertOrUpdateAssets(_:)`](facegroupanalyzer/insertorupdateassets(_:).md) to detect faces and persist the results. The method returns an async sequence of asset identifier and [`FaceGroupAnalyzer.Face`](facegroupanalyzer/face.md) array pairs, one for each image. This example creates assets from an array of image URLs and iterates through the detection results:

```swift
let assets = imageURLs.map { url in
    MediaIntelligenceImageAsset(
        id: MediaIntelligenceImageAsset.ID(url.lastPathComponent),
        kind: .url(url)
    )
}

let results = try await analyzer.insertOrUpdateAssets(assets)
for try await (assetID, faces) in results {
    for face in faces {
        print("Found face \(face.id) at \(face.bounds) in asset \(face.assetID).")
    }
}
```

Each detected face provides valid values for its [`id`](facegroupanalyzer/face/id-swift.property.md), [`bounds`](facegroupanalyzer/face/bounds.md), and [`assetID`](facegroupanalyzer/face/assetid.md) properties, but its [`entityID`](facegroupanalyzer/face/entityid.md) property is `nil`. The analyzer assigns this value when you group faces by person in the next step.

#### Group Faces By Person

The [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) method groups detected faces by person. Check the analyzer’s [`state`](facegroupanalyzer/state-swift.property.md) property to determine whether you need to run grouping. The property returns one of three values:

- **[`FaceGroupAnalyzer.State.ready`](facegroupanalyzer/state-swift.enum/ready.md)**: All faces have current group assignments.
- **[`FaceGroupAnalyzer.State.stale`](facegroupanalyzer/state-swift.enum/stale.md)**: You added, updated, or removed faces and need to run grouping.
- **[`FaceGroupAnalyzer.State.updating`](facegroupanalyzer/state-swift.enum/updating.md)**: The grouping algorithm is running.

> **Note**: If the app exits while the analyzer is updating, the state returns to [`FaceGroupAnalyzer.State.stale`](facegroupanalyzer/state-swift.enum/stale.md) on the next launch. Previously stored face data is preserved, so calling [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) again completes the grouping.

When the state is [`FaceGroupAnalyzer.State.stale`](facegroupanalyzer/state-swift.enum/stale.md), call [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) to run grouping:

```swift
if await analyzer.state == .stale {
    try await analyzer.update()
}
```

After the call to [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) completes, every detected face receives an [`entityID`](facegroupanalyzer/face/entityid.md) that groups it with other faces of the same person. The analyzer’s state returns to [`FaceGroupAnalyzer.State.ready`](facegroupanalyzer/state-swift.enum/ready.md).

#### Retrieve Face and Entity Data

After grouping completes, iterate all faces grouped by person using [`allFacesByEntityID`](facegroupanalyzer/allfacesbyentityid.md). Each element pairs an entity identifier that represents a unique person with an array of every face the analyzer detected for that person across all images:

```swift
for try await (entityID, faces) in analyzer.allFacesByEntityID {
    // Use entityID and faces to build person-based features.
}
```

To narrow your query, call [`fetchFaces(for:)`](facegroupanalyzer/fetchfaces(for:).md) or [`fetchAssetIDs(for:)`](facegroupanalyzer/fetchassetids(for:).md) with specific entity identifiers. These methods return synchronously from the local store, so they don’t require `await`.

#### Identify Faces Without Storing Data

To recognize people in new images without adding them to the analyzer’s persistent store, use the [`identifyFaces(in:)`](facegroupanalyzer/identifyfaces(in:).md) method. It detects faces in the provided images and matches them against the existing stored data. Returned faces include an [`entityID`](facegroupanalyzer/face/entityid.md) when they match a known person, letting you recognize people in newly captured photos or tag previews before saving to the persistent store.

Call this method when the analyzer’s state is [`FaceGroupAnalyzer.State.ready`](facegroupanalyzer/state-swift.enum/ready.md) or [`FaceGroupAnalyzer.State.stale`](facegroupanalyzer/state-swift.enum/stale.md). For best accuracy, call [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) first to ensure the stored data is fully grouped. When the state is stale, identification still works but produces less accurate results.

The following example identifies faces in a new image and filters for matches:

```swift
let asset = MediaIntelligenceImageAsset(
    id: MediaIntelligenceImageAsset.ID(newPhotoURL.lastPathComponent),
    kind: .url(newPhotoURL)
)

let results = try await analyzer.identifyFaces(in: [asset])
for try await (assetID, faces) in results {
    let matchedFaces = faces.filter { $0.entityID != nil }
    // The result contains faces that match known people in the stored data.
}
```

#### Manage Stored Data

The analyzer provides several options for removing stored data, from deleting individual assets to purging the entire working directory:

```swift
// Remove specific assets and their face data.
try await analyzer.deleteAssets([assetID1, assetID2])

// Remove all assets from the analyzer.
try await analyzer.deleteAllAssets()

// Remove all data from the working directory permanently.
try await FaceGroupAnalyzer.purge(workingDirectory: workingDirectory)
```

> ❗ **Important**: Calling [`purge(workingDirectory:)`](facegroupanalyzer/purge(workingdirectory:).md) permanently deletes all face data, group assignments, and metadata.

After deleting assets, the analyzer’s state becomes [`FaceGroupAnalyzer.State.stale`](facegroupanalyzer/state-swift.enum/stale.md) if any faces remain. Existing group assignments for the remaining faces are still valid, but calling [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) regroups them to account for the removed data.

## See Also

- [class FaceGroupAnalyzer](facegroupanalyzer.md)
  An object that detects faces in images and groups them by person.
- [struct MediaIntelligenceImageAsset](mediaintelligenceimageasset.md)
  An image asset to analyze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/detecting-and-grouping-faces-in-images)*