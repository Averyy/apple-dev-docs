# SecKeychainSetDomainSearchList(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the keychain search list for a specified preference domain.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainSetDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: CFArray) -> OSStatus
```

```c
OSStatus SecKeychainSetDomainSearchList(SecPreferencesDomain domain, CFArrayRef searchList);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to set the keychain search list for a specific preference domain. Use the [`SecKeychainSetSearchList(_:)`](./seckeychainsetsearchlist%28_%29.md) function if you want to set the keychain search list for the current preference domain. See the [`SecKeychainSetPreferenceDomain(_:)`](./seckeychainsetpreferencedomain%28_%29.md) function for a discussion of current and default preference domains.

## Parameters

- `domain`: The preference domain for which you wish to set the default keychain search list. See [`SecPreferencesDomain`](./secpreferencesdomain.md)for possible domain values.
- `searchList`: A pointer to a keychain search list to set in the preference domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetdomainsearchlist(_:_:))*