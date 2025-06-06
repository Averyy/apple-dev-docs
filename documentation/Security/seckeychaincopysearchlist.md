# SecKeychainCopySearchList(_:)

**Framework**: Security  
**Kind**: func

Retrieves a keychain search list.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainCopySearchList(_ searchList: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `searchList`: On return, the returned keychain search list. In Objective-C, call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincopysearchlist(_:))*