# init(currencyAmountResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a resolution result object with the specified currency amount resolution result object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(currencyAmountResolutionResult: INCurrencyAmountResolutionResult)
```

```objc
- (instancetype) initWithCurrencyAmountResolutionResult:(INCurrencyAmountResolutionResult *) currencyAmountResolutionResult;
```

## Return Value

An initialized resolution result object.

## Discussion

Typically, you do not call this method directly. Instead, you use the existing methods to create a resolution result of the appropriate type.

## Parameters

- `currencyAmountResolutionResult`: The [`INCurrencyAmountResolutionResult`](../incurrencyamountresolutionresult.md) object representing your proposed solution.

## See Also

### Creating a Resolution Result Object
- [class func unsupported(forReason: INRequestPaymentCurrencyAmountUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that the specified value is not supported.
- [enum INRequestPaymentCurrencyAmountUnsupportedReason](../inrequestpaymentcurrencyamountunsupportedreason.md)
  Constants indicating the reason for being unable to resolve the currency amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentcurrencyamountresolutionresult/init(currencyamountresolutionresult:))*