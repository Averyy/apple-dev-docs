# SecKeychainSetDefault(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the default keychain.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainSetDefault(_ keychain: SecKeychain?) -> OSStatus
```

```c
OSStatus SecKeychainSetDefault(SecKeychainRef keychain);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). The result code [`errSecNoSuchKeychain`](./errsecnosuchkeychain.md) indicates that the specified keychain could not be found. The result code [`errSecInvalidKeychain`](./errsecinvalidkeychain.md) indicates that the specified keychain is invalid.

#### Discussion

In most cases, your application should not need to set the default keychain, because this is a choice normally made by the user. You may call this function to change where a password or other keychain items are added, but since this is a user choice, you should set the default keychain back to the user specified keychain when you are done.

## Parameters

- `keychain`: A reference to the keychain you wish to make the default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetdefault(_:))*