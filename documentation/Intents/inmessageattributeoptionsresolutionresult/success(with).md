# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified attribute.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedMessageAttributeOptions: INMessageAttributeOptions = []) -> Self
```

```objc
+ (instancetype) successWithResolvedMessageAttributeOptions:(INMessageAttributeOptions) resolvedMessageAttributeOptions;
```

## Return Value

A new [`INMessageAttributeOptionsResolutionResult`](../inmessageattributeoptionsresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to resolve the parameter successfully to a recognizable value in your app.

## Parameters

- `resolvedMessageAttributeOptions`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INMessageAttributeOptions) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessageattributeoptionsresolutionresult/success(with:))*