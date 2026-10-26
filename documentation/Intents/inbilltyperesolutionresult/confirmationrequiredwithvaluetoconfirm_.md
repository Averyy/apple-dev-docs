# confirmationRequiredWithValueToConfirm:

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.3+ - Deprecated in 11.0
- iPadOS 10.3+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
+ (instancetype) confirmationRequiredWithValueToConfirm:(INBillType) valueToConfirm;
```

## See Also

### Creating a Resolution Result Object
- [class func success(with: INBillType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.
- [class func confirmationRequired(with: INBillType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilltyperesolutionresult/confirmationrequiredwithvaluetoconfirm:)*