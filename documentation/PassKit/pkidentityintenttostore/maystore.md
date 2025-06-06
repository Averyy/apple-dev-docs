# mayStore

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An object that indicates your app may store a data element for an indefinite length of time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class var mayStore: PKIdentityIntentToStore { get }
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

## See Also

- [class var willNotStore: PKIdentityIntentToStore](pkidentityintenttostore/willnotstore.md)
  An object that indicates your app won’t store a data element any longer than necessary to complete a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityintenttostore/maystore)*