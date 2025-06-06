# SecKeychainCopyDomainDefault(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the default keychain from a specified preference domain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainCopyDomainDefault(_ domain: SecPreferencesDomain, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to retrieve the default keychain for a specific preference domain. Use the [`SecKeychainCopyDefault(_:)`](seckeychaincopydefault(_:).md) function if you want the default keychain for the current preference domain. See the [`SecKeychainSetPreferenceDomain(_:)`](seckeychainsetpreferencedomain(_:).md) function for a discussion of current and default preference domains.

## Parameters

- `domain`: The preference domain from which you wish to retrieve the default keychain. See   for possible domain values.
- `keychain`: On return, a pointer to the keychain object of the default keychain in the specified preference domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincopydomaindefault(_:_:))*