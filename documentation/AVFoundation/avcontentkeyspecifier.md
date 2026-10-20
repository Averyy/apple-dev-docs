# AVContentKeySpecifier

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that uniquely identifies a content key.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
class AVContentKeySpecifier
```

```objc
@interface AVContentKeySpecifier : NSObject
```

## Topics

### Creating a specifier
- [init(forKeySystem: AVContentKeySystem, identifier: Any, options: [String : Any])](./avcontentkeyspecifier/init%28forkeysystem,identifier,options%29.md)
  Creates a content key specifier.
### Inspecting a specifier
- [var identifier: any Sendable](./avcontentkeyspecifier/identifier.md)
  The container and protocol-specific key identifier.
- [var keySystem: AVContentKeySystem](./avcontentkeyspecifier/keysystem.md)
  The key system that generates content keys.
- [var options: [String : any Sendable]](./avcontentkeyspecifier/options.md)
  A dictionary of options with which you initialized the specifier.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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
- [class AVContentKeyRequest](./avcontentkeyrequest.md)
  An object that encapsulates information about a content decryption key request issued from a content key session object.
- [class AVPersistableContentKeyRequest](./avpersistablecontentkeyrequest.md)
  An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [class AVContentKeyResponse](./avcontentkeyresponse.md)
  An object that encapsulates information about a response to a content decryption key request.
- [enum AVExternalContentProtectionStatus](./avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.
- [func AVSampleBufferAttachContentKey(CMSampleBuffer, AVContentKey, NSErrorPointer) -> Bool](./avsamplebufferattachcontentkey%28_,_,_%29.md)
  Attaches a content key to a sample buffer for the purpose of content decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyspecifier)*