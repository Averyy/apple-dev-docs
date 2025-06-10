# KEM.Errors

**Framework**: Apple CryptoKit  
**Kind**: enum

Errors that CryptoKit throws when it encounters problems in key encapsulation mechanism (KEM) operations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 2.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum Errors
```

## Topics

### Enumeration Cases
- [KEM.Errors.invalidSeed](kem/errors/invalidseed.md)
  The seed value supplied for deriving a key isn’t valid.
- [KEM.Errors.publicKeyMismatchDuringInitialization](kem/errors/publickeymismatchduringinitialization.md)
  The public key CryptoKit receives when it initializes a key encapsulation operation doesn’t match the expected value.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kem/errors)*