# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a resolution object that indicates the successful resolution of the provided value.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedCarSignalOptions: INCarSignalOptions = []) -> Self
```

```objc
+ (instancetype) successWithResolvedCarSignalOptions:(INCarSignalOptions) resolvedCarSignalOptions;
```

## Return Value

A new [`INCarSignalOptionsResolutionResult`](../incarsignaloptionsresolutionresult.md) object.

## Discussion

Use this method to create a result object when you are able to resolve a parameter successfully.

## Parameters

- `resolvedCarSignalOptions`: The value that resolves the [`signals`](../inactivatecarsignalintent/signals.md) property of the activate car signal intent. This value may be different from the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INCarSignalOptions) -> Self](./confirmationrequired%28with%29.md)
  Creates a resolution object that requires confirmation of the provided value.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incarsignaloptionsresolutionresult/success(with:))*