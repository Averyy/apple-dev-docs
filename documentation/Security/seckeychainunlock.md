# SecKeychainUnlock(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Unlocks a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainUnlock(_ keychain: SecKeychain?, _ passwordLength: UInt32, _ password: UnsafeRawPointer?, _ usePassword: Bool) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). The result code [`errSecUserCanceled`](errsecusercanceled.md) indicates that the user pressed the Cancel button in the Unlock Keychain dialog box. The result code [`errSecAuthFailed`](errsecauthfailed.md) indicates that authentication failed because of too many unsuccessful retries. The result code [`errSecInteractionRequired`](errsecinteractionrequired.md) indicates that user interaction is required to unlock the keychain.

#### Discussion

In most cases, your application does not need to call this function directly, since most Keychain Services functions that require an unlocked keychain do so for you. If your application needs to verify that a keychain is unlocked, call the function [`SecKeychainGetStatus(_:_:)`](seckeychaingetstatus(_:_:).md).

## Parameters

- `keychain`: A reference to the keychain to unlock. Pass   to specify the default keychain. If you pass a locked keychain, this function displays the Unlock Keychain dialog box if you have not provided a password. If the specified keychain is currently unlocked, the Unlock Keychain dialog box is not displayed and this function returns  . You must call the   function to release this object when you are finished using it.
- `passwordLength`: An unsigned 32-bit integer representing the length of the password buffer.
- `password`: A buffer containing the password for the keychain. Pass   if the user password is unknown. In this case, this function displays the Unlock Keychain dialog to prompt the user for the keychain password.
- `usePassword`: A Boolean value indicating whether the password parameter is used. You should pass   if you are passing a password or   if it is to be ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainunlock(_:_:_:_:))*