# Loading media data asynchronously

**Framework**: AVFoundation

Build responsive apps by using language-level concurrency features to efficiently load media data.

#### Overview

AVFoundation uses the [`AVAsset`](avasset.md) class to model timed audiovisual media. Creating an asset is a lightweight operation because it defers loading its media until it requires the data. How long it takes an asset to load its data depends on factors, including the media’s size, local device capabilities, and remote network conditions. To avoid blocking the calling thread, you must load media data asynchronously.

> ❗ **Important**:  Starting in iOS 16, tvOS 16, MacCatalyst 16, and macOS 13, AVFoundation deprecates using the synchronous properties and methods of [`AVAsset`](avasset.md), [`AVAssetTrack`](avassettrack.md), and [`AVMetadataItem`](avmetadataitem.md) for Swift clients. It also deprecates loading property values asynchronously using the [`loadValuesAsynchronously(forKeys:completionHandler:)`](avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys:completionhandler:).md) method in favor of the syntax described below.

 Starting in iOS 16, tvOS 16, MacCatalyst 16, and macOS 13, AVFoundation deprecates using the synchronous properties and methods of [`AVAsset`](avasset.md), [`AVAssetTrack`](avassettrack.md), and [`AVMetadataItem`](avmetadataitem.md) for Swift clients. It also deprecates loading property values asynchronously using the [`loadValuesAsynchronously(forKeys:completionHandler:)`](avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys:completionhandler:).md) method in favor of the syntax described below.

##### Load Properties Asynchronously

The framework builds its asynchronous property-loading capabilities around two key types: [`AVAsyncProperty`](avasyncproperty.md) and [`AVAsynchronousKeyValueLoading`](avasynchronouskeyvalueloading.md). The framework uses the [`AVAsyncProperty`](avasyncproperty.md) class to define type-safe identifiers for properties with values that require asynchronous loading, and uses the [`AVAsynchronousKeyValueLoading`](avasynchronouskeyvalueloading.md) protocol to define the interface for objects to load properties asynchronously. [`AVAsset`](avasset.md), [`AVAssetTrack`](avassettrack.md), and [`AVMetadataItem`](avmetadataitem.md) adopt this protocol, which provides them an asynchronous [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method with the following signature:

```swift
public func load<T>(_ property: AVAsyncProperty<Self, T>) async throws -> T
```

Call this method from an asynchronous context, and specify the `await` keyword to indicate that execution can suspend until it finishes loading the data. The method returns a type-safe value if it successfully loads the property, or throws an error if it fails.

```swift
// A CMTime value.
let duration = try await asset.load(.duration)
// An array of AVMetadataItem for the asset.
let metadata = try await asset.load(.metadata)
```

If you know in advance that you require loading several asset properties, you can use a variation of the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method that takes multiple identifiers and returns its result in a tuple. Like loading a single property value, loading several properties at the same time is also a type-safe operation.

```swift
// A CMTime value and an array of AVMetadataItem.
let (duration, metadata) = try await asset.load(.duration, .metadata)
```

> **Note**:  Loading several properties at the same time enables AVFoundation to optimize performance by batch-loading requests.

 Loading several properties at the same time enables AVFoundation to optimize performance by batch-loading requests.

##### Determine a Property Status

[`AVAsynchronousKeyValueLoading`](avasynchronouskeyvalueloading.md) also provides a [`status(of:)`](avasynchronouskeyvalueloading/status(of:).md) method that returns the status of a property identifier. It returns an [`AVAsyncProperty.Status`](avasyncproperty/status.md) value that indicates the state of the property’s value using the cases shown in the example below:

```swift
// Determine the loaded status of the metadata property.
switch asset.status(of: .metadata) {
case .notYetLoaded:
    // The initial state of a property.
case .loading:
    // The asset is actively loading the property value.
case .loaded(let metadata):
    // The property is ready to use.
case .failed(let error):
    // The property value fails to load.
}
```

The `.loaded` and `.failed` cases provide an associated value. The `.loaded` case contains the previously loaded property value, and the `.failed` case contains an error that indicates the reason for the failure. Having access to an associated value enables you to perform operations like checking a property’s status and accessing its value in a single step.

```swift
// Verify the metadata property is in a loaded state.
if case .loaded(let metadata) = asset.status(of: .metadata) {
    // Process the loaded value.
    processMetadata(metadata)
}
```

##### Filter Property Collections

Some properties provide arrays of values, such as an asset’s [`tracks`](avpartialasyncproperty/tracks-44ptx.md) or its [`metadata`](avpartialasyncproperty/metadata-16qej.md). In many cases, you’re interested in only a subset of those values. [`AVAsset`](avasset.md) and [`AVAssetTrack`](avassettrack.md) also provide methods to filter their collections to only the values that you require. For example, the code listing below determines the audio sample rates that an asset contains. It calls the asset’s [`loadTracks(withMediaType:completionHandler:)`](avasset/loadtracks(withmediatype:completionhandler:).md) to retrieve only its audio tracks. It iterates over each track and asynchronously loads the track’s format descriptions. Finally, it retrieves the sample rates from the stream description and sorts the results.

```swift
// Load the asset's audio tracks asynchronously.
let audioTracks = try await asset.loadTracks(withMediaType: .audio)
var allDescriptions = [CMFormatDescription]()
for track in audioTracks {
    // Load each audio track's format descriptions asynchronously.
    allDescriptions.append(contentsOf: try await track.load(.formatDescriptions))
}
// Collect the unique sample rates, and sort them from highest to lowest.
let sampleRates = Set(allDescriptions).map {
    Float($0.audioStreamBasicDescription?.mSampleRate ?? 0)
}.sorted(by: { $0 > $1 })
```

Using Swift concurrency and the AVFoundation asynchronous APIs makes performing even advanced inspection, as shown above, a simple, straight-line operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/loading-media-data-asynchronously)*