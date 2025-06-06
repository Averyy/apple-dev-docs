# identifier

**Framework**: StoreKit Test  
**Kind**: property

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

#### Discussion

To get a list of all the transactions available in the testing environment, see [`allTransactions()`](sktestsession/alltransactions().md).

Use this [`identifier`](sktesttransaction/identifier.md) if you want to perform actions on the transaction in the testing environment, such as:

- [`approveAskToBuyTransaction(identifier:)`](sktestsession/approveasktobuytransaction(identifier:).md)
- [`consentToPriceIncreaseForTransaction(identifier:)`](sktestsession/consenttopriceincreasefortransaction(identifier:).md)
- [`declineAskToBuyTransaction(identifier:)`](sktestsession/declineasktobuytransaction(identifier:).md)
- [`declinePriceIncreaseForTransaction(identifier:)`](sktestsession/declinepriceincreasefortransaction(identifier:).md)
- [`deleteTransaction(identifier:)`](sktestsession/deletetransaction(identifier:).md)
- [`disableAutoRenewForTransaction(identifier:)`](sktestsession/disableautorenewfortransaction(identifier:).md)
- [`enableAutoRenewForTransaction(identifier:)`](sktestsession/enableautorenewfortransaction(identifier:).md)
- [`refundTransaction(identifier:)`](sktestsession/refundtransaction(identifier:).md)
- [`requestPriceIncreaseConsentForTransaction(identifier:)`](sktestsession/requestpriceincreaseconsentfortransaction(identifier:).md)
- [`resolveIssueForTransaction(identifier:)`](sktestsession/resolveissuefortransaction(identifier:).md)

## See Also

- [var originalTransactionIdentifier: Int](sktesttransaction/originaltransactionidentifier.md)
  The identifier of the original transaction.
- [var productIdentifier: String](sktesttransaction/productidentifier.md)
  An identifier that uniquely represents a product, which you provide in the StoreKit configuration file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/identifier)*