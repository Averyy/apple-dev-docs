# shapedArrayValue(of:)

**Framework**: Core ML  
**Kind**: method

Returns the underlying shaped array of the feature value.

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
func shapedArrayValue<Scalar>(of type: Scalar.Type) -> MLShapedArray<Scalar>? where Scalar : MLShapedArrayScalar
```

## Parameters

- `type`: The scalar type of the underlying shaped array.

## See Also

- [var isUndefined: Bool](mlfeaturevalue/isundefined.md)
  A Boolean value that indicates whether the feature value is undefined or missing.
- [var int64Value: Int64](mlfeaturevalue/int64value.md)
  The underlying integer of the feature value.
- [var doubleValue: Double](mlfeaturevalue/doublevalue.md)
  The underlying double of the feature value.
- [var stringValue: String](mlfeaturevalue/stringvalue.md)
  The underlying string of the feature value.
- [var imageBufferValue: CVPixelBuffer?](mlfeaturevalue/imagebuffervalue.md)
  The underlying image of the feature value as a pixel buffer.
- [var multiArrayValue: MLMultiArray?](mlfeaturevalue/multiarrayvalue.md)
  The underlying multiarray of the feature value.
- [var sequenceValue: MLSequence?](mlfeaturevalue/sequencevalue.md)
  The underlying sequence of the feature value.
- [var dictionaryValue: [AnyHashable : NSNumber]](mlfeaturevalue/dictionaryvalue.md)
  The underlying dictionary of the feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/shapedarrayvalue(of:))*