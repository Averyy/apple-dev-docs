# url

**Framework**: ProximityReader  
**Kind**: property

The URL to display to the customer if the matching loyalty or reward ID isn’t found.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
let url: URL?
```

## Mentions

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)

#### Discussion

If the customer isn’t part of the merchant’s loyalty program, they can use the provided URL to get more information about that program.

## See Also

- [let shouldSendURLOnly: Bool](vasrequest/merchant/shouldsendurlonly.md)
  A Boolean value that indicates whether to send only the merchant URL to the customer’s device without requesting data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasrequest/merchant/url)*