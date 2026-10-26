# confirmationRequiredWithValueToConfirm:

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

## Declaration

```objc
+ (instancetype) confirmationRequiredWithValueToConfirm:(INPaymentStatus) valueToConfirm;
```

## See Also

### Creating a Resolution Result Object
- [class func success(with: INPaymentStatus) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func confirmationRequired(with: INPaymentStatus) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatusresolutionresult/confirmationrequiredwithvaluetoconfirm:)*