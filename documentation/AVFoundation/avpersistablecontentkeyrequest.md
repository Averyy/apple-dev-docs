# AVPersistableContentKeyRequest

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that encapsulates information about a persistable content decryption key request issued from a content key session.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class AVPersistableContentKeyRequest
```

```objc
@interface AVPersistableContentKeyRequest : AVContentKeyRequest
```

## Overview

This class allows clients to create and use persistable content keys.

## Topics

### Requesting persistable content key data
- [func persistableContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](./avpersistablecontentkeyrequest/persistablecontentkey%28fromkeyvendorresponse,options%29.md)
  Creates a persistable content key from the content key context data.

## Relationships

### Inherits From
- [AVContentKeyRequest](./avcontentkeyrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
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
- [class AVContentKeyResponse](./avcontentkeyresponse.md)
  An object that encapsulates information about a response to a content decryption key request.
- [enum AVExternalContentProtectionStatus](./avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.
- [func AVSampleBufferAttachContentKey(CMSampleBuffer, AVContentKey, NSErrorPointer) -> Bool](./avsamplebufferattachcontentkey%28_,_,_%29.md)
  Attaches a content key to a sample buffer for the purpose of content decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpersistablecontentkeyrequest)*