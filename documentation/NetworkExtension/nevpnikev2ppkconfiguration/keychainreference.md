# keychainReference

**Framework**: Network Extension  
**Kind**: property

A persistent reference to the key in the keychain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var keychainReference: Data { get }
```

#### Discussion

The keychain item needs to have the class [`kSecClassGenericPassword`](https://developer.apple.com/documentation/Security/kSecClassGenericPassword).

## See Also

- [var identifier: String](nevpnikev2ppkconfiguration/identifier.md)
  The identifier for the PPK.
- [var isMandatory: Bool](nevpnikev2ppkconfiguration/ismandatory.md)
  A Boolean value that indicates whether it’s mandatory for the VPN server to use this PPK.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2ppkconfiguration/keychainreference)*