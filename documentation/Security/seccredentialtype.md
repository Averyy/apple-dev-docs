# SecCredentialType

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The credential type to be returned by [`SecKeyGetCredentials`](./seckeygetcredentials.md).

**Availability**:
- macOS 10.3+ - Deprecated in 12.0

> **Deprecated**: No longer supported

## Declaration

```swift
enum SecCredentialType
```

```c
enum SecCredentialType : uint32;
```

## Overview

See the section “Servers and the Keychain” in the [macOS Keychain Services Tasks](https://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/03tasks/tasks.html#//apple_ref/doc/uid/TP30000897-CH205) chapter of [Keychain Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000897) for information on the use of UI with keychain tasks.

## Topics

### Constants
- [SecCredentialType.default](./seccredentialtype/default.md)
  The default setting for determining whether to present UI is used.
- [SecCredentialType.withUI](./seccredentialtype/withui.md)
  Keychain operations on keys that have this credential are allowed to present UI if required.
- [SecCredentialType.noUI](./seccredentialtype/noui.md)
  Keychain operations on keys that have this credential are not allowed to present UI, and will fail if UI is required.
### Initializers
- [init?(rawValue: uint32)](./seccredentialtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccredentialtype)*