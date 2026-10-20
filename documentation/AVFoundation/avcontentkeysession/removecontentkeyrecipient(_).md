# removeContentKeyRecipient(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to remove the specified recipient.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func removeContentKeyRecipient(_ recipient: any AVContentKeyRecipient)
```

```objc
- (void) removeContentKeyRecipient:(id<AVContentKeyRecipient>) recipient;
```

## Parameters

- `recipient`: The content key recipient to remove.

## See Also

### Managing content key recipients
- [var contentKeyRecipients: [any AVContentKeyRecipient]](./contentkeyrecipients.md)
  An array of content key recipients.
- [protocol AVContentKeyRecipient](../avcontentkeyrecipient.md)
  A protocol for requiring decryption keys for media data.
- [func addContentKeyRecipient(any AVContentKeyRecipient)](./addcontentkeyrecipient%28_%29.md)
  Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/removecontentkeyrecipient(_:))*