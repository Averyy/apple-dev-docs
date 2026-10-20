# contentKeyRecipients

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of content key recipients.

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
var contentKeyRecipients: [any AVContentKeyRecipient] { get }
```

```objc
@property (readonly) NSArray<id<AVContentKeyRecipient>> * contentKeyRecipients;
```

## See Also

### Managing content key recipients
- [protocol AVContentKeyRecipient](../avcontentkeyrecipient.md)
  A protocol for requiring decryption keys for media data.
- [func addContentKeyRecipient(any AVContentKeyRecipient)](./addcontentkeyrecipient%28_%29.md)
  Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.
- [func removeContentKeyRecipient(any AVContentKeyRecipient)](./removecontentkeyrecipient%28_%29.md)
  Tells the delegate to remove the specified recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/contentkeyrecipients)*