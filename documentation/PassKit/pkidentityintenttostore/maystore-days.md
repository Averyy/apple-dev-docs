# mayStore(days:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

An object that indicates your app may store a data element for the length of time you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class func mayStore(days: Int) -> Self
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

#### Return Value

A new instance of [`PKIdentityIntentToStore`](pkidentityintenttostore.md).

## Parameters

- `days`: The length of time to store a data element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityintenttostore/maystore(days:))*