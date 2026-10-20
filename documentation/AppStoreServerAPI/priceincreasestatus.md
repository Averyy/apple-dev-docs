# priceIncreaseStatus

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The status that indicates whether an auto-renewable subscription is subject to a price increase.

**Availability**:
- App Store Server API 1.0+

## Declaration

```
int32 priceIncreaseStatus
```

## Possible Values

- `0`: The customer hasn’t yet responded to an auto-renewable subscription price increase that requires customer consent.
- `1`: The customer consented to an auto-renewable subscription price increase that requires customer consent, or the App Store has notified the customer of an auto-renewable subscription price increase that doesn’t require consent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/priceincreasestatus)*