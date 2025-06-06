# SecKeychainGetPreferenceDomain(_:)

**Framework**: Security  
**Kind**: func

Gets the current keychain preference domain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainGetPreferenceDomain(_ domain: UnsafeMutablePointer<SecPreferencesDomain>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. The default preference domain for system daemons (that is, for daemons running in the root session) is the system domain. The default preference domain for all other programs is the user domain. Use the [`SecKeychainSetPreferenceDomain(_:)`](seckeychainsetpreferencedomain(_:).md) function to change the preference domain.

## Parameters

- `domain`: On return, a pointer to the keychain preference domain. See   for possible domain values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetpreferencedomain(_:))*