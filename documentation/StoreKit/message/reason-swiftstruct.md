# Message.Reason

**Framework**: StoreKit  
**Kind**: struct

Reasons for the App Store messages.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Reason
```

#### Overview

The message reason informs your app of the purpose of the message. Your app can optionally use this information when it handles the messages.

For information about handling App Store messages, see [`Message`](message.md).

## Topics

### Getting the message reasons
- [static let billingIssue: Message.Reason](message/reason-swift.struct/billingissue.md)
  A message the App Store sends that informs people of a billing problem and enables them to update billing information.
- [static let generic: Message.Reason](message/reason-swift.struct/generic.md)
  A message the App Store sends for a generic reason.
- [static let priceIncreaseConsent: Message.Reason](message/reason-swift.struct/priceincreaseconsent.md)
  A message the App Store sends when you increase the price of an auto-renewable subscription and the price increase requires the customer’s consent.
- [static let winBackOffer: Message.Reason](message/reason-swift.struct/winbackoffer.md)
  A message the App Store sends when the customer is eligible for a win-back offer that you configure in App Store Connect.
### Getting the localized description
- [var localizedDescription: String](message/reason-swift.struct/localizeddescription.md)
  A localized description of the App Store message.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Message](message.md)
  An instance for receiving and displaying App Store messages in your app.
- [struct DisplayMessageAction](displaymessageaction.md)
  An instance that asks StoreKit to display an App Store message, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/message/reason-swift.struct)*