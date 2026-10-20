# CKShare.AccessRequester

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class AccessRequester
```

```objc
@interface CKShareAccessRequester : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./accessrequester/init%28coder%29.md)
### Instance Properties
- [var contact: CNContact](./accessrequester/contact.md)
  A displayable CNContact representing the requester.
- [var participantLookupInfo: CKUserIdentity.LookupInfo](./accessrequester/participantlookupinfo.md)
  Lookup information for the requester.
- [var userIdentity: CKUserIdentity](./accessrequester/useridentity.md)
  The identity of the user requesting access to the share.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/accessrequester)*