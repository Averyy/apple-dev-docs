# SecCredentialType

**Framework**: Security  
**Kind**: enum

The credential type to be returned by [`SecKeyGetCredentials`](seckeygetcredentials.md).

**Availability**:
- macOS 10.3+

## Declaration

```swift
enum SecCredentialType
```

#### Overview

See the section “Servers and the Keychain” in the [`macOS Keychain Services Tasks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/03tasks/tasks.html#//apple_ref/doc/uid/TP30000897-CH205) chapter of [`Keychain Services Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000897) for information on the use of UI with keychain tasks.

## Topics

### Constants
- [SecCredentialType.default](seccredentialtype/default.md)
  The default setting for determining whether to present UI is used.
- [SecCredentialType.withUI](seccredentialtype/withui.md)
  Keychain operations on keys that have this credential are allowed to present UI if required.
- [SecCredentialType.noUI](seccredentialtype/noui.md)
  Keychain operations on keys that have this credential are not allowed to present UI, and will fail if UI is required.
### Initializers
- [init?(rawValue: uint32)](seccredentialtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccredentialtype)*