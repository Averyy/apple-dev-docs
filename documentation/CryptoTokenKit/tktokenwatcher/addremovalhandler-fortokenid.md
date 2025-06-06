# addRemovalHandler(_:forTokenID:)

**Framework**: CryptoTokenKit  
**Kind**: method

Adds a removal handler for the specified token ID.

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
func addRemovalHandler(_ removalHandler: @escaping (String) -> Void, forTokenID tokenID: String)
```

## Mentions

- [Using Cryptographic Assets Stored on a Smart Card](using-cryptographic-assets-stored-on-a-smart-card.md)

#### Discussion

You typically call this method in the `insertionHandler` passed to the token watcher initializer.

Adding a removal handler will remove any existing removal handlers for the specified token ID.

## Parameters

- `removalHandler`: A block to be called when the specified token is removed. This block takes a single argument:
- `tokenID`: If   doesn’t contain  ,   is executed immediately.

## See Also

- [func setInsertionHandler((String) -> Void)](tktokenwatcher/setinsertionhandler(_:).md)
  Sets an insertion handler closure to be called when a new token is inserted into the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/addremovalhandler(_:fortokenid:))*