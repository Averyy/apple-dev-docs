# shapedArrayValue(of:)

**Framework**: Core ML  
**Kind**: method

Returns the shaped array value, if the contained value is a shaped array of the specified type.

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
func shapedArrayValue<Scalar>(of type: Scalar.Type) -> MLShapedArray<Scalar>? where Scalar : MLShapedArrayScalar
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsendablefeaturevalue/shapedarrayvalue(of:))*