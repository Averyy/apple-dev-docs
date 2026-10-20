# init(shapedArray:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a feature value that contains a shaped array.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init<Scalar>(shapedArray: MLShapedArray<Scalar>) where Scalar : MLShapedArrayScalar
```

## Parameters

- `shapedArray`: An [`MLShapedArray`](../mlshapedarray.md) instance.

## See Also

### Creating multidimensional feature values
- [convenience init(multiArray: MLMultiArray)](./init%28multiarray%29.md)
  Creates a feature value that contains a multidimensional array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/init(shapedarray:))*