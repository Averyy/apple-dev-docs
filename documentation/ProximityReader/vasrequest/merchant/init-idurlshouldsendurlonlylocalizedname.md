# init(id:url:shouldSendURLOnly:localizedName:)

**Framework**: ProximityReader  
**Kind**: init

Creates a new merchant object with the specified information.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
init(id: String, url: URL? = nil, shouldSendURLOnly: Bool = false, localizedName: String? = nil)
```

## Parameters

- `id`: The merchant’s unique identifier. Obtain this value from the merchant.
- `url`: The URL to display if the customer doesn’t belong to the merchant’s loyalty program.
- `shouldSendURLOnly`: A Boolean value that indicates whether to send the URL information to the customer’s device.
- `localizedName`: The name of the merchant, localized for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasrequest/merchant/init(id:url:shouldsendurlonly:localizedname:))*