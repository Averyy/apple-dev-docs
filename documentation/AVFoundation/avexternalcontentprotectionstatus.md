# AVExternalContentProtectionStatus

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that specify whether sufficient protection exists to display the content.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
enum AVExternalContentProtectionStatus
```

```c
enum AVExternalContentProtectionStatus : NSInteger;
```

## Topics

### Status values
- [AVExternalContentProtectionStatus.pending](./avexternalcontentprotectionstatus/pending.md)
  A status that indicates content protections are pending.
- [AVExternalContentProtectionStatus.sufficient](./avexternalcontentprotectionstatus/sufficient.md)
  A status that indicates sufficient protections exists for display.
- [AVExternalContentProtectionStatus.insufficient](./avexternalcontentprotectionstatus/insufficient.md)
  A status that indicates insufficient protections exists for display.
### Initializers
- [init?(rawValue: Int)](./avexternalcontentprotectionstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### FairPlay streaming
- [class AVContentKeySession](./avcontentkeysession.md)
  An object that creates and tracks decryption keys for media data.
- [protocol AVContentKeySessionDelegate](./avcontentkeysessiondelegate.md)
  A protocol that handles content key requests.
- [class AVContentKey](./avcontentkey.md)
  An object that represents the content key decryptor.
- [class AVContentKeySpecifier](./avcontentkeyspecifier.md)
  An object that uniquely identifies a content key.
- [class AVContentKeyRequest](./avcontentkeyrequest.md)
  An object that encapsulates information about a content decryption key request issued from a content key session object.
- [class AVPersistableContentKeyRequest](./avpersistablecontentkeyrequest.md)
  An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [class AVContentKeyResponse](./avcontentkeyresponse.md)
  An object that encapsulates information about a response to a content decryption key request.
- [func AVSampleBufferAttachContentKey(CMSampleBuffer, AVContentKey, NSErrorPointer) -> Bool](./avsamplebufferattachcontentkey%28_,_,_%29.md)
  Attaches a content key to a sample buffer for the purpose of content decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalcontentprotectionstatus)*