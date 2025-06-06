# tokenIDs

**Framework**: CryptoTokenKit  
**Kind**: property

The token IDs currently available in the system.

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
var tokenIDs: [String] { get }
```

## Mentions

- [Using Cryptographic Assets Stored on a Smart Card](using-cryptographic-assets-stored-on-a-smart-card.md)

#### Discussion

Each string in [`tokenIDs`](tktokenwatcher/tokenids.md) corresponds to the name of the token instance.

You can observe this property to be notified of additions and removals to system tokens. See [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/tokenids)*