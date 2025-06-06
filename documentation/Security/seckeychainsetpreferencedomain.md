# SecKeychainSetPreferenceDomain(_:)

**Framework**: Security  
**Kind**: func

Sets the keychain preference domain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainSetPreferenceDomain(_ domain: SecPreferencesDomain) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. The default preference domain for system daemons (that is, for daemons running in the root session) is the system domain. The default preference domain for all other programs is the user domain.

This function changes the preference domain for all subsequent function calls; for example, if you change from the system domain to the user domain and then call [`SecKeychainLock(_:)`](seckeychainlock(_:).md) specifying `NULL` for the keychain, the function locks the default system keychain rather than the default user keychain. You might want to use this function, for example, when launching a system daemon from a user session so that the daemon uses system preferences rather than user preferences.

## Parameters

- `domain`: The keychain preference domain to set. See   for possible domain values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetpreferencedomain(_:))*