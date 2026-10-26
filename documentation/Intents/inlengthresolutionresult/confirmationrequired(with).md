# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func confirmationRequired(with lengthToConfirm: Measurement<UnitLength>?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithLengthToConfirm:(NSMeasurement<NSUnitLength *> *) lengthToConfirm;
```

#### Return Value

A new [`INLengthResolutionResult`](../inlengthresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to the specified object but you want the user to confirm that value.

## Parameters

- `lengthToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Objects
- [class func success(with: Measurement<UnitLength>) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [Measurement<UnitLength>]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlengthresolutionresult/confirmationrequired(with:))*