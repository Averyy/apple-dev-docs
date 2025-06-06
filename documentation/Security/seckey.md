# SecKey

**Framework**: Security  
**Kind**: class

An object that represents a cryptographic key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SecKey
```

## Mentions

- [Getting an Existing Key](getting-an-existing-key.md)

#### Overview

A [`SecKey`](seckey.md) instance that represents a key that is stored in a keychain can be safely cast to a [`SecKeychainItem`](seckeychainitem.md) for manipulation as a keychain item. On the other hand, if the key is not stored in a keychain, casting the object to a [`SecKeychainItem`](seckeychainitem.md) and passing it to Keychain Services functions returns errors.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckey)*