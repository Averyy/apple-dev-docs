# AVSampleBufferAttachContentKey(_:_:_:)

**Framework**: AVFoundation  
**Kind**: func  
**Role**: Function

Attaches a content key to a sample buffer for the purpose of content decryption.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 14.5+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use CMReadySampleBuffer.attach(contentKey:) instead

## Declaration

```swift
func AVSampleBufferAttachContentKey(_ sbuf: CMSampleBuffer, _ contentKey: AVContentKey, _ outError: NSErrorPointer) -> Bool
```

```c
extern BOOL AVSampleBufferAttachContentKey(CMSampleBufferRef sbuf, AVContentKey *contentKey, NSError **outError);
```

#### Return Value

A Boolean value that indicates whether the attachment is successful.

## Parameters

- `sbuf`: The sample buffer to which to attach the content key.
- `contentKey`: The content key to attach.
- `outError`: An error pointer. If a failure occurs, the system sets the pointer to an error object that describes the details of the failure.

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
- [enum AVExternalContentProtectionStatus](./avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferattachcontentkey(_:_:_:))*