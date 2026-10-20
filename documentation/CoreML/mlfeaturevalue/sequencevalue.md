# sequenceValue

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The underlying sequence of the feature value.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var sequenceValue: MLSequence? { get }
```

```objc
@property (nonatomic, readonly, nullable) MLSequence * sequenceValue;
```

## See Also

### Accessing the feature’s value
- [var isUndefined: Bool](./isundefined.md)
  A Boolean value that indicates whether the feature value is undefined or missing.
- [var int64Value: Int64](./int64value.md)
  The underlying integer of the feature value.
- [var doubleValue: Double](./doublevalue.md)
  The underlying double of the feature value.
- [var stringValue: String](./stringvalue.md)
  The underlying string of the feature value.
- [var imageBufferValue: CVPixelBuffer?](./imagebuffervalue.md)
  The underlying image of the feature value as a pixel buffer.
- [func shapedArrayValue<Scalar>(of: Scalar.Type) -> MLShapedArray<Scalar>?](./shapedarrayvalue%28of%29.md)
  Returns the underlying shaped array of the feature value.
- [var multiArrayValue: MLMultiArray?](./multiarrayvalue.md)
  The underlying multiarray of the feature value.
- [var dictionaryValue: [AnyHashable : NSNumber]](./dictionaryvalue.md)
  The underlying dictionary of the feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/sequencevalue)*