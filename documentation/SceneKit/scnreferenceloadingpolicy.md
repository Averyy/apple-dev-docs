# SCNReferenceLoadingPolicy

**Framework**: SceneKit  
**Kind**: enum

Options for when to load the reference node’s content, used by the [`loadingPolicy`](scnreferencenode/loadingpolicy.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SCNReferenceLoadingPolicy
```

## Topics

### Constants
- [SCNReferenceLoadingPolicy.immediate](scnreferenceloadingpolicy/immediate.md)
  Load the node’s external content immediately when the reference node is unarchived.
- [SCNReferenceLoadingPolicy.onDemand](scnreferenceloadingpolicy/ondemand.md)
  Load the node’s external comment only when the [`load()`](scnreferencenode/load().md) method is called.
### Initializers
- [init?(rawValue: Int)](scnreferenceloadingpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy)*