# declinePriceIncreaseForTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Simulates a user canceling an auto-renewable subscription by disabling auto-renew.

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
func declinePriceIncreaseForTransaction(identifier: Int) throws
```

```objc
- (BOOL) declinePriceIncreaseForTransactionWithIdentifier:(NSUInteger) identifier error:(NSError **) error;
```

## Discussion

To test how your app handles the price increase consent flow for auto-renewable subscriptions, first call [`requestPriceIncreaseConsentForTransaction(identifier:)`](./requestpriceincreaseconsentfortransaction%28identifier%29.md).

Call [`declinePriceIncreaseForTransaction(identifier:)`](./declinepriceincreasefortransaction%28identifier%29.md) to simulate a user canceling the subscription. Specifically, this method disables auto-renew and removes the subscription’s pending price increase status. The subscription expires at the end of the billing period in the testing environment.

## Parameters

- `identifier`: The transaction [`identifier`](../sktesttransaction/identifier.md) of the auto-renewable subscription that has a pending price increase.

## See Also

### Testing price increase consent
- [func requestPriceIncreaseConsentForTransaction(identifier: Int) throws](./requestpriceincreaseconsentfortransaction%28identifier%29.md)
  Simulates a price increase that requires customer consent for an auto-renewable subscription.
- [func consentToPriceIncreaseForTransaction(identifier: Int) throws](./consenttopriceincreasefortransaction%28identifier%29.md)
  Simulates a user consenting to a price increase for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/declinepriceincreasefortransaction(identifier:))*