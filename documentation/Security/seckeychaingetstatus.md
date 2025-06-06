# SecKeychainGetStatus(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves status information of a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainGetStatus(_ keychain: SecKeychain?, _ keychainStatus: UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). The result code [`errSecNoSuchKeychain`](errsecnosuchkeychain.md) indicates that the specified keychain could not be found. The result code [`errSecInvalidKeychain`](errsecinvalidkeychain.md) indicates that the specified keychain is invalid.

#### Discussion

This function retrieves the status of a specified keychain. You can use this function to determine if the keychain is unlocked, readable, or writable. Note that the lock status of a keychain can change at any time due to user or system activity. Because the system automatically prompts the user to unlock a keychain when necessary, you do not usually have to worry about the lock status of a keychain. If you do need to track the lock status of a keychain, use the [`SecKeychainAddCallback(_:_:_:)`](seckeychainaddcallback(_:_:_:).md) function to register for keychain notifications.

## Parameters

- `keychain`: A keychain object of the keychain whose status you wish to determine for the user session. Pass   to obtain the status of the default keychain.
- `keychainStatus`: On return, a pointer to the status of the specified keychain. See   for valid status constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetstatus(_:_:))*