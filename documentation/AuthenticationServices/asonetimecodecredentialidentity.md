# ASOneTimeCodeCredentialIdentity

**Framework**: Authentication Services  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class ASOneTimeCodeCredentialIdentity
```

#### Overview

An ASOneTimeCodeCredentialIdentity is used to describe an identity that can use a service upon successful one-time code based authentication. Use this class to save entries into ASCredentialIdentityStore.

## Topics

### Initializers
- [init?(coder: NSCoder)](asonetimecodecredentialidentity/init(coder:).md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, label: String, recordIdentifier: String?)](asonetimecodecredentialidentity/init(serviceidentifier:label:recordidentifier:).md)
### Instance Properties
- [var label: String](asonetimecodecredentialidentity/label.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [ASCredentialIdentity](ascredentialidentity.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asonetimecodecredentialidentity)*