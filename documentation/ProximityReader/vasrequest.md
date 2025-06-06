# VASRequest

**Framework**: ProximityReader  
**Kind**: class

A request to read a contactless loyalty card and retrieve loyalty program identifiers for the person.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
class VASRequest
```

## Mentions

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)

#### Overview

Create a `VASRequest` object to obtain details from someone’s loyalty card so that you can process associated transactions. After you create this object, pass it to the [`readVAS(_:)`](paymentcardreadersession/readvas(_:).md)or [`readPaymentCard(_:vasRequest:stopOnVASResult:)`](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:).md) method of [`PaymentCardReaderSession`](paymentcardreadersession.md).

## Topics

### Creating a loyalty card request
- [init(vasMerchants: [VASRequest.Merchant], localizedVASType: String)](vasrequest/init(vasmerchants:localizedvastype:).md)
  Creates a request to read loyalty card service information.
### Getting the loyalty card details
- [let localizedVASType: String](vasrequest/localizedvastype.md)
  The localized name of the loyalty program.
- [let vasMerchants: [VASRequest.Merchant]](vasrequest/vasmerchants.md)
  The list of merchants to match against the user’s Wallet content or loyalty card.
- [VASRequest.Merchant](vasrequest/merchant.md)
  The identity of a merchant that offers a loyalty program.
### Setting the user interface language
- [var userInterfaceLanguage: Locale.Language?](vasrequest/userinterfacelanguage.md)
  The language to use when localizing the user interface.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)
  Set up the necessary components so your app can begin using Tap to Pay on iPhone to read and issue loyalty passes.
- [struct VASReadResult](vasreadresult.md)
  The result of a request to read loyalty card information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasrequest)*