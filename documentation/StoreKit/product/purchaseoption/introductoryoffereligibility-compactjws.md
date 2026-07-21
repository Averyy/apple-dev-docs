# introductoryOfferEligibility(compactJWS:)

**Framework**: StoreKit  
**Kind**: method

Set the eligibility of an introductory offer for a purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
static func introductoryOfferEligibility(compactJWS: String) -> Product.PurchaseOption
```

## Mentions

- [Generating JWS to sign App Store requests](generating-jws-to-sign-app-store-requests.md)

#### Discussion

For information about generating and signing this JWT, see [`Include custom claims for introductory offer eligibility`](generating-jws-to-sign-app-store-requests#Include-custom-claims-for-introductory-offer-eligibility.md).

## Parameters

- `compactJWS`: The signed JWT string with the introductory offer eligibility for the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/introductoryoffereligibility(compactjws:))*