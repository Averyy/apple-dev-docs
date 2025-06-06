# consentToPriceIncreaseForTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method

Simulates a user consenting to a price increase for an auto-renewable subscription.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
func consentToPriceIncreaseForTransaction(identifier: Int) throws
```

#### Discussion

To test how your app handles the price increase consent flow for auto-renewable subscriptions, first call [`requestPriceIncreaseConsentForTransaction(identifier:)`](sktestsession/requestpriceincreaseconsentfortransaction(identifier:).md).

Call the [`consentToPriceIncreaseForTransaction(identifier:)`](sktestsession/consenttopriceincreasefortransaction(identifier:).md) method to simulate a user consenting to the price increase. This method removes the subscription’s pending price increase status. The subscription renews at the next billing period.

## Parameters

- `identifier`: The transaction   of the auto-renewable subscription that has a pending price increase.

## See Also

- [func requestPriceIncreaseConsentForTransaction(identifier: Int) throws](sktestsession/requestpriceincreaseconsentfortransaction(identifier:).md)
  Simulates a price increase that requires customer consent for an auto-renewable subscription.
- [func declinePriceIncreaseForTransaction(identifier: Int) throws](sktestsession/declinepriceincreasefortransaction(identifier:).md)
  Simulates a user canceling an auto-renewable subscription by disabling auto-renew.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/consenttopriceincreasefortransaction(identifier:))*