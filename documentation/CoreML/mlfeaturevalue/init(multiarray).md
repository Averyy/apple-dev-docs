# init(multiArray:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a feature value that contains a multidimensional array.

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
convenience init(multiArray value: MLMultiArray)
```

```objc
+ (instancetype) featureValueWithMultiArray:(MLMultiArray *) value;
```

## Parameters

- `value`: An [`MLMultiArray`](../mlmultiarray.md) instance.

## See Also

### Creating multidimensional feature values
- [convenience init<Scalar>(shapedArray: MLShapedArray<Scalar>)](./init%28shapedarray%29.md)
  Creates a feature value that contains a shaped array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/init(multiarray:))*