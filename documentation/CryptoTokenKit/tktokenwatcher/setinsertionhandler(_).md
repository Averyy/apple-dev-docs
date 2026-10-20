# setInsertionHandler(_:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Sets an insertion handler closure to be called when a new token is inserted into the system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func setInsertionHandler(_ insertionHandler: @escaping (String) -> Void)
```

```objc
- (void) setInsertionHandler:(void (^)(NSString *tokenID)) insertionHandler;
```

## Mentions

- [Using Cryptographic Assets Stored on a Smart Card](../using-cryptographic-assets-stored-on-a-smart-card.md)

## Parameters

- `insertionHandler`: A closure to be called whenever a token is added to the system. The closure takes a single argument, the tokenID, that identifies the added token.

## See Also

### Configuring Handlers
- [func addRemovalHandler((String) -> Void, forTokenID: String)](./addremovalhandler%28_,fortokenid%29.md)
  Adds a removal handler for the specified token ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/setinsertionhandler(_:))*