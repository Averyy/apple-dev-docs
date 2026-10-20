# failTransactionsEnabled

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether transactions fail in the testing environment.

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
var failTransactionsEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL failTransactionsEnabled;
```

#### Discussion

The default value is `false`. Set this value to `true` when you want to test your app’s response to [`SKPaymentTransaction`](../../StoreKit/skpaymenttransaction.md) transactions that fail. Attempted transactions in the payment queue show the [`SKPaymentTransactionState.failed`](../../StoreKit/skpaymenttransactionstate/failed.md) state, with the error code that you set in [`failureError`](./failureerror.md).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](./resettodefaultstate%28%29.md) to revert all settings to those in the configuration file.

## See Also

### Forcing failed transactions
- [var failureError: SKError.Code](./failureerror.md)
  The error code that transactions return when you enable failing transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/failtransactionsenabled)*