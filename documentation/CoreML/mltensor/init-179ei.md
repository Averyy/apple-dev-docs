# init(_:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor from a ML shaped array.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init<ShapedArray>(_ shapedArray: ShapedArray) where ShapedArray : MLShapedArrayProtocol, ShapedArray.Scalar : MLTensorScalar
```

## Parameters

- `shapedArray`: The shaped array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(_:)-179ei)*