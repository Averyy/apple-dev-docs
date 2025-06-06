# fill(with:)

**Framework**: CryptoTokenKit  
**Kind**: method

Fills the keychain with the specified items.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func fill(with items: [TKTokenKeychainItem])
```

#### Discussion

All existing items for the token are first removed from the keychain before filling the keychain with `items`.

## Parameters

- `items`: The items to be added to the keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/fill(with:))*