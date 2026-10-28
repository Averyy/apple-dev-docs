# keychainReference

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSData * keychainReference;
```

## Discussion

The keychain item needs to have the class [`kSecClassGenericPassword`](../../Security/ksecclassgenericpassword.md).

## See Also

### Accessing the configuration parameters
- [var identifier: String](./identifier.md)
  The identifier for the PPK.
- [var isMandatory: Bool](./ismandatory.md)
  A Boolean value that indicates whether it’s mandatory for the VPN server to use this PPK.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2ppkconfiguration/keychainreference)*