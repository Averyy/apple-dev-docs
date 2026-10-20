# SecKeychainItem

**Framework**: Security  
**Kind**: class  
**Role**: Class

An opaque type that represents a keychain item.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class SecKeychainItem
```

```c
typedef struct __SecKeychainItem * SecKeychainItemRef;
```

#### Overview

A [`SecKeychainItem`](./seckeychainitem.md) object for a certificate that is stored in a keychain can be safely cast to a [`SecCertificate`](./seccertificate.md) for use with [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md).

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitem)*