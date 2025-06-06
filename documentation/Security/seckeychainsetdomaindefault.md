# SecKeychainSetDomainDefault(_:_:)

**Framework**: Security  
**Kind**: func

Sets the default keychain for a specified preference domain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainSetDomainDefault(_ domain: SecPreferencesDomain, _ keychain: SecKeychain?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to set the default keychain for a specific preference domain. Use the [`SecKeychainSetDefault(_:)`](seckeychainsetdefault(_:).md) function if you want to set the default keychain for the current preference domain. See the [`SecKeychainSetPreferenceDomain(_:)`](seckeychainsetpreferencedomain(_:).md) function for a discussion of current and default preference domains.

## Parameters

- `domain`: The preference domain for which you wish to set the default keychain. See   for possible domain values.
- `keychain`: A reference to the keychain you wish to set as default in the specified preference domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetdomaindefault(_:_:))*