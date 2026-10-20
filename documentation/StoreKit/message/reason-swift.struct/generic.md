# generic

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A message the App Store sends for a generic reason.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
static let generic: Message.Reason
```

## See Also

### Getting the message reasons
- [static let billingIssue: Message.Reason](./billingissue.md)
  A message the App Store sends that informs people of a billing problem and enables them to update billing information.
- [static let priceIncreaseConsent: Message.Reason](./priceincreaseconsent.md)
  A message the App Store sends when you increase the price of an auto-renewable subscription and the price increase requires the customer’s consent.
- [static let winBackOffer: Message.Reason](./winbackoffer.md)
  A message the App Store sends when the customer is eligible for a win-back offer that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/message/reason-swift.struct/generic)*