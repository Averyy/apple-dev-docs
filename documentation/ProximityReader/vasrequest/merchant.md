# VASRequest.Merchant

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

The identity of a merchant that offers a loyalty program.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Merchant
```

## Mentions

- [Accepting loyalty passes from Wallet](../accepting-loyalty-passes-from-wallet.md)

## Overview

Create `Merchant` objects to identify merchants whose loyalty programs you support. When placing a request for loyalty card information, or Value Added Services (VAS) information, specify the associated merchant details. The system uses the merchant information to return details only for those merchants.

## Topics

### Creating a merchant structure
- [init(id: String, url: URL?, shouldSendURLOnly: Bool, localizedName: String?)](./merchant/init%28id,url,shouldsendurlonly,localizedname%29.md)
  Creates a new merchant object with the specified information.
### Getting the merchant name
- [var localizedName: String](./merchant/localizedname.md)
  The localized name of the merchant or corresponding loyalty program.
### Getting the merchant URL details
- [let url: URL?](./merchant/url.md)
  The URL to display to the customer if the matching loyalty or reward ID isn’t found.
- [let shouldSendURLOnly: Bool](./merchant/shouldsendurlonly.md)
  A Boolean value that indicates whether to send only the merchant URL to the customer’s device without requesting data.
### Getting the merchant ID
- [let id: String](./merchant/id.md)
  A unique identifier for the merchant.
### Initializers
- [init(id: String, url: URL?, localizedName: String?)](./merchant/init%28id,url,localizedname%29.md)
  Creates a new merchant object with the specified information.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the loyalty card details
- [let localizedVASType: String](./localizedvastype.md)
  The localized name of the loyalty program.
- [let vasMerchants: [VASRequest.Merchant]](./vasmerchants.md)
  The list of merchants to match against the user’s Wallet content or loyalty card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasrequest/merchant)*