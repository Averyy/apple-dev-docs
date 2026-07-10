# addPass(_:)

**Framework**: ProximityReader  
**Kind**: method

Asks the customer to confirm adding a Pass to Wallet.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func addPass(_ pass: Data) async throws -> Bool
```

## Mentions

- [Adding support for Tap to Share to your app](adding-support-for-tap-to-share-to-your-app.md)

#### Return Value

`true` if the pass is added to Wallet successfully or the same pass already exists; `false` if the customer declines.

#### Discussion

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails.

## Parameters

- `pass`: Properly created `.pkpass` data to be added to Wallet. The `passTypeIdentifier` of the pass must be one of the identifiers in the [`passTypeIdentifiers`](customerengagementsession/configuration-swift.struct/passtypeidentifiers.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/addpass(_:))*