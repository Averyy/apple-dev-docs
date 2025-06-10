# AVSampleBufferAttachContentKey(_:_:_:)

**Framework**: AVFoundation  
**Kind**: func

Attaches a content key to a sample buffer for the purpose of content decryption.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func AVSampleBufferAttachContentKey(_ sbuf: CMSampleBuffer, _ contentKey: AVContentKey, _ outError: NSErrorPointer) -> Bool
```

#### Return Value

A Boolean value that indicates whether the attachment is successful.

## Parameters

- `sbuf`: The sample buffer to which to attach the content key.
- `contentKey`: The content key to attach.
- `outError`: An error pointer. If a failure occurs, the system sets the pointer to an error object that describes the details of the failure.

## See Also

- [class AVContentKeySession](avcontentkeysession.md)
  An object that creates and tracks decryption keys for media data.
- [protocol AVContentKeySessionDelegate](avcontentkeysessiondelegate.md)
  A protocol that handles content key requests.
- [class AVContentKey](avcontentkey.md)
  An object that represents the content key decryptor.
- [class AVContentKeySpecifier](avcontentkeyspecifier.md)
  An object that uniquely identifies a content key.
- [class AVContentKeyRequest](avcontentkeyrequest.md)
  An object that encapsulates information about a content decryption key request issued from a content key session object.
- [class AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md)
  An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [class AVContentKeyResponse](avcontentkeyresponse.md)
  An object that encapsulates information about a response to a content decryption key request.
- [enum AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferattachcontentkey(_:_:_:))*