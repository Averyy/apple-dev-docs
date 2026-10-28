# SecKeychainCopySearchList(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves a keychain search list.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainCopySearchList(_ searchList: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

```c
OSStatus SecKeychainCopySearchList(CFArrayRef*searchList);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `searchList`: On return, the returned keychain search list. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincopysearchlist(_:))*