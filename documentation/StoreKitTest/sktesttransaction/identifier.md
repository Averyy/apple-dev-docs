# identifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The identifier of the transaction in the testing environment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var identifier: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger identifier;
```

#### Discussion

To get a list of all the transactions available in the testing environment, see [`allTransactions()`](../sktestsession/alltransactions%28%29.md).

Use this [`identifier`](./identifier.md) if you want to perform actions on the transaction in the testing environment, such as:

- [`approveAskToBuyTransaction(identifier:)`](../sktestsession/approveasktobuytransaction%28identifier%29.md)
- [`consentToPriceIncreaseForTransaction(identifier:)`](../sktestsession/consenttopriceincreasefortransaction%28identifier%29.md)
- [`declineAskToBuyTransaction(identifier:)`](../sktestsession/declineasktobuytransaction%28identifier%29.md)
- [`declinePriceIncreaseForTransaction(identifier:)`](../sktestsession/declinepriceincreasefortransaction%28identifier%29.md)
- [`deleteTransaction(identifier:)`](../sktestsession/deletetransaction%28identifier%29.md)
- [`disableAutoRenewForTransaction(identifier:)`](../sktestsession/disableautorenewfortransaction%28identifier%29.md)
- [`enableAutoRenewForTransaction(identifier:)`](../sktestsession/enableautorenewfortransaction%28identifier%29.md)
- [`refundTransaction(identifier:)`](../sktestsession/refundtransaction%28identifier%29.md)
- [`requestPriceIncreaseConsentForTransaction(identifier:)`](../sktestsession/requestpriceincreaseconsentfortransaction%28identifier%29.md)
- [`resolveIssueForTransaction(identifier:)`](../sktestsession/resolveissuefortransaction%28identifier%29.md)

## See Also

### Identifying Transactions and Products
- [var originalTransactionIdentifier: Int](./originaltransactionidentifier.md)
  The identifier of the original transaction.
- [var productIdentifier: String](./productidentifier.md)
  An identifier that uniquely represents a product, which you provide in the StoreKit configuration file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/identifier)*