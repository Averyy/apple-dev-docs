# SCNReferenceLoadingPolicy

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Options for when to load the reference node’s content, used by the [`loadingPolicy`](./scnreferencenode/loadingpolicy.md) property.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum SCNReferenceLoadingPolicy
```

```c
enum SCNReferenceLoadingPolicy : NSInteger;
```

## Topics

### Constants
- [SCNReferenceLoadingPolicy.immediate](./scnreferenceloadingpolicy/immediate.md)
  Load the node’s external content immediately when the reference node is unarchived.
- [SCNReferenceLoadingPolicy.onDemand](./scnreferenceloadingpolicy/ondemand.md)
  Load the node’s external comment only when the [`load()`](./scnreferencenode/load%28%29.md) method is called.
### Initializers
- [init?(rawValue: Int)](./scnreferenceloadingpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy)*