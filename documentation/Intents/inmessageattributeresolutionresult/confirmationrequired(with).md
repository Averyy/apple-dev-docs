# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with messageAttributeToConfirm: INMessageAttribute) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithMessageAttributeToConfirm:(INMessageAttribute) messageAttributeToConfirm;
```

## Return Value

A new [`INMessageAttributeResolutionResult`](../inmessageattributeresolutionresult.md) object.

## Discussion

Use this method when you can resolve the parameter to a single value but want the user to confirm that value.

## Parameters

- `messageAttributeToConfirm`: The value that resolves the request but that must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INMessageAttribute) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessageattributeresolutionresult/confirmationrequired(with:))*