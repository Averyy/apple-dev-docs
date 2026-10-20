# AVContentKeyRecipient

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A protocol for requiring decryption keys for media data.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol AVContentKeyRecipient
```

```objc
@protocol AVContentKeyRecipient
```

## Topics

### Verifying decryption key requirements
- [var mayRequireContentKeysForMediaDataProcessing: Bool](./avcontentkeyrecipient/mayrequirecontentkeysformediadataprocessing.md)
  A Boolean value that indicates whether the recipient requires decryption keys for media data to enable processing.
- [func contentKeySession(AVContentKeySession, didProvide: AVContentKey)](./avcontentkeyrecipient/contentkeysession%28_,didprovide%29.md)
  Tells the recipient that a content key is available.

## Relationships

### Conforming Types
- [AVFragmentedAsset](./avfragmentedasset.md)
- [AVURLAsset](./avurlasset.md)

## See Also

### Managing content key recipients
- [var contentKeyRecipients: [any AVContentKeyRecipient]](./avcontentkeysession/contentkeyrecipients.md)
  An array of content key recipients.
- [func addContentKeyRecipient(any AVContentKeyRecipient)](./avcontentkeysession/addcontentkeyrecipient%28_%29.md)
  Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.
- [func removeContentKeyRecipient(any AVContentKeyRecipient)](./avcontentkeysession/removecontentkeyrecipient%28_%29.md)
  Tells the delegate to remove the specified recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrecipient)*