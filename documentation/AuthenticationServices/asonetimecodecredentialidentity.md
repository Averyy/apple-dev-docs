# ASOneTimeCodeCredentialIdentity

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASOneTimeCodeCredentialIdentity : NSObject
```

## Overview

An ASOneTimeCodeCredentialIdentity is used to describe an identity that can use a service upon successful one-time code based authentication. Use this class to save entries into ASCredentialIdentityStore.

## Topics

### Initializers
- [init?(coder: NSCoder)](./asonetimecodecredentialidentity/init%28coder%29.md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, label: String, recordIdentifier: String?)](./asonetimecodecredentialidentity/init%28serviceidentifier,label,recordidentifier%29.md)
### Instance Properties
- [var label: String](./asonetimecodecredentialidentity/label.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASCredentialIdentity](./ascredentialidentity.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asonetimecodecredentialidentity)*