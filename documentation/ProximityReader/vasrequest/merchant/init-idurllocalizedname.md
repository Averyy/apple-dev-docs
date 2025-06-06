# init(id:url:localizedName:)

**Framework**: ProximityReader  
**Kind**: init

Creates a new merchant object with the specified information.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
init(id: String, url: URL? = nil, localizedName: String? = nil)
```

## Parameters

- `id`: The merchant’s unique identifier. Obtain this value from the merchant.
- `url`: The URL to display if the customer doesn’t belong to the merchant’s loyalty program.
- `localizedName`: The name of the merchant, localized for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasrequest/merchant/init(id:url:localizedname:))*