# SecKeychainSetSearchList(_:)

**Framework**: Security  
**Kind**: func

Specifies the list of keychains to use in the default keychain search list.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainSetSearchList(_ searchList: CFArray) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The default keychain search list is used by several functions; see for example [`SecKeychainSearchCreateFromAttributes`](seckeychainsearchcreatefromattributes.md), [`SecKeychainFindInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](seckeychainfindinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md), or [`SecKeychainFindGenericPassword(_:_:_:_:_:_:_:_:)`](seckeychainfindgenericpassword(_:_:_:_:_:_:_:_:).md). To obtain the current default keychain search list, use the [`SecKeychainCopySearchList(_:)`](seckeychaincopysearchlist(_:).md) function.

The default keychain search list is displayed as the keychain list in the Keychain Access utility. If you use [`SecKeychainSetSearchList(_:)`](seckeychainsetsearchlist(_:).md) to change the keychain search list, the list displayed in Keychain Access changes accordingly.

## Parameters

- `searchList`: An array of keychain references (of type  ) specifying the list of keychains to use in the default keychain search list. Passing an empty array clears the search list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetsearchlist(_:))*