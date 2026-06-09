# update(subprogress:)

**Framework**: Media Intelligence  
**Kind**: method

Clusters faces into entities and updates their assignments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func update(subprogress: consuming Subprogress? = nil) async throws
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Discussion

Call this method after ingesting assets with [`insertOrUpdateAssets(_:)`](facegroupanalyzer/insertorupdateassets(_:).md) to run the face clustering algorithm. When this method completes, every face has a non-nil [`entityID`](facegroupanalyzer/face/entityid.md) and [`state`](facegroupanalyzer/state-swift.property.md) returns [`FaceGroupAnalyzer.State.ready`](facegroupanalyzer/state-swift.enum/ready.md).

If the analyzer is already up to date, this method returns immediately without performing any clustering.

## Parameters

- `subprogress`: An optional subprogress object for reporting progress to a parent `Progress`.

## See Also

- [var state: FaceGroupAnalyzer.State](facegroupanalyzer/state-swift.property.md)
  A value describing the current processing state of the analyzer.
- [FaceGroupAnalyzer.State](facegroupanalyzer/state-swift.enum.md)
  The current processing state of a face group analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/update(subprogress:))*