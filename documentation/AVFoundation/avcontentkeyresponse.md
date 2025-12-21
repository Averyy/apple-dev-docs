# AVContentKeyResponse

**Framework**: AVFoundation  
**Kind**: class

An object that encapsulates information about a response to a content decryption key request.

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
class AVContentKeyResponse
```

## Topics

### Creating new content key responses
- [convenience init(clearKeyData: Data, initializationVector: Data?)](avcontentkeyresponse/init(clearkeydata:initializationvector:).md)
  Creates a new key response object for key data and initialization vector sent in the clear.
- [convenience init(fairPlayStreamingKeyResponseData: Data)](avcontentkeyresponse/init(fairplaystreamingkeyresponsedata:).md)
  Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.
- [convenience init(authorizationTokenData: Data)](avcontentkeyresponse/init(authorizationtokendata:).md)
  Creates a content key response with an authorization token.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [enum AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.
- [func AVSampleBufferAttachContentKey(CMSampleBuffer, AVContentKey, NSErrorPointer) -> Bool](avsamplebufferattachcontentkey(_:_:_:).md)
  Attaches a content key to a sample buffer for the purpose of content decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse)*