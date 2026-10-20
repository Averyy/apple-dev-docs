# SecKeychainFreeAttributeInfo(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Releases the memory acquired by calling the `SecKeychainAttributeInfoForItemID` function.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainFreeAttributeInfo(_ info: UnsafeMutablePointer<SecKeychainAttributeInfo>) -> OSStatus
```

```c
OSStatus SecKeychainFreeAttributeInfo(SecKeychainAttributeInfo *info);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `info`: A pointer to the keychain attribute information to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainfreeattributeinfo(_:))*