# addContentKeyRecipient(_:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func addContentKeyRecipient(_ recipient: any AVContentKeyRecipient)
```

#### Discussion

Don’t add a recipient to a session that has expired or had already begun to process media data.

## Parameters

- `recipient`: The content key recipient to use for the session.

## See Also

- [var contentKeyRecipients: [any AVContentKeyRecipient]](avcontentkeysession/contentkeyrecipients.md)
  An array of content key recipients.
- [protocol AVContentKeyRecipient](avcontentkeyrecipient.md)
  A protocol for requiring decryption keys for media data.
- [func removeContentKeyRecipient(any AVContentKeyRecipient)](avcontentkeysession/removecontentkeyrecipient(_:).md)
  Tells the delegate to remove the specified recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/addcontentkeyrecipient(_:))*