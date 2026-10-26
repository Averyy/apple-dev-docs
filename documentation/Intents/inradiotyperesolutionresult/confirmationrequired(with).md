# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class func confirmationRequired(with radioTypeToConfirm: INRadioType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithRadioTypeToConfirm:(INRadioType) radioTypeToConfirm;
```

#### Return Value

A new [`INRadioTypeResolutionResult`](../inradiotyperesolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to an equivalent radio type and want the user to confirm the replacement value before proceeding.

## Parameters

- `radioTypeToConfirm`: The value that resolves the request but the user needs to confirm it.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INRadioType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inradiotyperesolutionresult/confirmationrequired(with:))*