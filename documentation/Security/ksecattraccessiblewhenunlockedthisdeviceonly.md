# kSecAttrAccessibleWhenUnlockedThisDeviceOnly

**Framework**: Security  
**Kind**: var

The data in the keychain item can be accessed only while the device is unlocked by the user.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFString
```

## Mentions

- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)

#### Discussion

This is recommended for items that need to be accessible only while the application is in the foreground. Items with this attribute  migrate to a new device. Thus, after restoring from a backup of a different device, these items will not be present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly)*