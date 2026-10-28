# failureError

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The error code that transactions return when you enable failing transactions.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- watchOS 7.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Use simulatedError(forAPI:)

## Declaration

```swift
var failureError: SKError.Code { get set }
```

```objc
@property (nonatomic, assign) SKErrorCode failureError;
```

## Discussion

You can force an error by setting [`failTransactionsEnabled`](./failtransactionsenabled.md) to `true` and setting [`failureError`](./failureerror.md) value to one of these supported error codes: [`SKError.Code.unknown`](../../StoreKit/skerror/code/unknown.md), [`SKError.Code.invalidOfferIdentifier`](../../StoreKit/skerror/code/invalidofferidentifier.md), [`SKError.Code.invalidSignature`](../../StoreKit/skerror/code/invalidsignature.md), [`SKError.Code.missingOfferParams`](../../StoreKit/skerror/code/missingofferparams.md), [`SKError.Code.invalidOfferPrice`](../../StoreKit/skerror/code/invalidofferprice.md).

Use these settings to test your how your app responds to failed transactions.

## See Also

### Forcing failed transactions
- [var failTransactionsEnabled: Bool](./failtransactionsenabled.md)
  A Boolean value that determines whether transactions fail in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/failureerror)*