# SecKeychainCopyDomainSearchList(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the keychain search list for a specified preference domain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainCopyDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to retrieve the keychain search list for a specific preference domain. Use the [`SecKeychainCopySearchList(_:)`](seckeychaincopysearchlist(_:).md) function if you want the keychain search list for the current preference domain. See the [`SecKeychainSetPreferenceDomain(_:)`](seckeychainsetpreferencedomain(_:).md) function for a discussion of current and default preference domains.

## Parameters

- `domain`: The preference domain from which you wish to retrieve the keychain search list. See   for possible domain values.
- `searchList`: On return, a pointer to the keychain search list of the specified preference domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincopydomainsearchlist(_:_:))*