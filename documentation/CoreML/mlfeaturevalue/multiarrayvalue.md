# multiArrayValue

**Framework**: Core ML  
**Kind**: property

The underlying multiarray of the feature value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var multiArrayValue: MLMultiArray? { get }
```

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
- [func shapedArrayValue<Scalar>(of: Scalar.Type) -> MLShapedArray<Scalar>?](mlfeaturevalue/shapedarrayvalue(of:).md)
  Returns the underlying shaped array of the feature value.
- [var sequenceValue: MLSequence?](mlfeaturevalue/sequencevalue.md)
  The underlying sequence of the feature value.
- [var dictionaryValue: [AnyHashable : NSNumber]](mlfeaturevalue/dictionaryvalue.md)
  The underlying dictionary of the feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/multiarrayvalue)*