# SecKeychainLock(_:)

**Framework**: Security  
**Kind**: func

Locks a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainLock(_ keychain: SecKeychain?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). The result code [`errSecNoSuchKeychain`](errsecnosuchkeychain.md) indicates that specified keychain could not be found. The result code [`errSecInvalidKeychain`](errsecinvalidkeychain.md) indicates that the specified keychain is invalid.

#### Discussion

Your application should not call this function unless you are responding to a user’s request to lock a keychain. In general, you should leave the keychain unlocked so that the user does not have to unlock it again in another application.

## Parameters

- `keychain`: A reference to the keychain to lock. Pass   to lock the default keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainlock(_:))*