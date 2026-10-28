# addContentKeyRecipient(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.

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
func addContentKeyRecipient(_ recipient: any AVContentKeyRecipient)
```

```objc
- (void) addContentKeyRecipient:(id<AVContentKeyRecipient>) recipient;
```

## Discussion

Don’t add a recipient to a session that has expired or had already begun to process media data.

## Parameters

- `recipient`: The content key recipient to use for the session.

## See Also

### Managing content key recipients
- [var contentKeyRecipients: [any AVContentKeyRecipient]](./contentkeyrecipients.md)
  An array of content key recipients.
- [protocol AVContentKeyRecipient](../avcontentkeyrecipient.md)
  A protocol for requiring decryption keys for media data.
- [func removeContentKeyRecipient(any AVContentKeyRecipient)](./removecontentkeyrecipient%28_%29.md)
  Tells the delegate to remove the specified recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/addcontentkeyrecipient(_:))*