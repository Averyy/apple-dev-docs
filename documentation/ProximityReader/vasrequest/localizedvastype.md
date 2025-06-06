# localizedVASType

**Framework**: ProximityReader  
**Kind**: property

The localized name of the loyalty program.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
final let localizedVASType: String
```

#### Discussion

Specify the loyalty program name, instead of a payment amount, when you request only a Value Added Services (VAS) read. The maximum length of this string is 22 characters.

## See Also

- [let vasMerchants: [VASRequest.Merchant]](vasrequest/vasmerchants.md)
  The list of merchants to match against the user’s Wallet content or loyalty card.
- [VASRequest.Merchant](vasrequest/merchant.md)
  The identity of a merchant that offers a loyalty program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasrequest/localizedvastype)*