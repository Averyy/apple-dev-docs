# FaceGroupAnalyzer.State

**Framework**: Media Intelligence  
**Kind**: enum  
**Role**: Enumeration

The current processing state of a face group analyzer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum State
```

## Overview

This type describes whether the analyzer’s face cluster assignments are up to date. Read [`state`](./state-swift.property.md) to check the current value before deciding whether to call [`update(subprogress:)`](./update%28subprogress%29.md).

## Topics

### States
- [FaceGroupAnalyzer.State.ready](./state-swift.enum/ready.md)
  A state that indicates all faces have up-to-date cluster assignments.
- [FaceGroupAnalyzer.State.stale](./state-swift.enum/stale.md)
  A state that indicates new faces need cluster assignments.
- [FaceGroupAnalyzer.State.updating](./state-swift.enum/updating.md)
  A state that indicates the clustering algorithm is running.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Updating the gallery
- [var state: FaceGroupAnalyzer.State](./state-swift.property.md)
  A value describing the current processing state of the analyzer.
- [func update(subprogress: consuming Subprogress?) async throws](./update%28subprogress%29.md)
  Clusters faces into entities and updates their assignments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/state-swift.enum)*