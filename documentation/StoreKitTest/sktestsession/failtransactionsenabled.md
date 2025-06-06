# failTransactionsEnabled

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that determines whether transactions fail in the testing environment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
var failTransactionsEnabled: Bool { get set }
```

#### Discussion

The default value is `false`. Set this value to `true` when you want to test your app’s response to [`SKPaymentTransaction`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction) transactions that fail. Attempted transactions in the payment queue show the [`SKPaymentTransactionState.failed`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransactionState/failed) state, with the error code that you set in [`failureError`](sktestsession/failureerror.md).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](sktestsession/resettodefaultstate().md) to revert all settings to those in the configuration file.

## See Also

- [var failureError: SKError.Code](sktestsession/failureerror.md)
  The error code that transactions return when you enable failing transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/failtransactionsenabled)*