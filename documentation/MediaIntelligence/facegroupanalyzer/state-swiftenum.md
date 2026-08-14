# FaceGroupAnalyzer.State

**Framework**: Media Intelligence  
**Kind**: enum

The current processing state of a face group analyzer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum State
```

#### Overview

This type describes whether the analyzer’s face cluster assignments are up to date. Read [`state`](facegroupanalyzer/state-swift.property.md) to check the current value before deciding whether to call [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md).

## Topics

### States
- [FaceGroupAnalyzer.State.ready](facegroupanalyzer/state-swift.enum/ready.md)
  A state that indicates all faces have up-to-date cluster assignments.
- [FaceGroupAnalyzer.State.stale](facegroupanalyzer/state-swift.enum/stale.md)
  A state that indicates new faces need cluster assignments.
- [FaceGroupAnalyzer.State.updating](facegroupanalyzer/state-swift.enum/updating.md)
  A state that indicates the clustering algorithm is running.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var state: FaceGroupAnalyzer.State](facegroupanalyzer/state-swift.property.md)
  A value describing the current processing state of the analyzer.
- [func update(subprogress: consuming Subprogress?) async throws](facegroupanalyzer/update(subprogress:).md)
  Clusters faces into entities and updates their assignments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/state-swift.enum)*