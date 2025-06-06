# SecKeychainFreeAttributeInfo(_:)

**Framework**: Security  
**Kind**: func

Releases the memory acquired by calling the `SecKeychainAttributeInfoForItemID` function.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainFreeAttributeInfo(_ info: UnsafeMutablePointer<SecKeychainAttributeInfo>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `info`: A pointer to the keychain attribute information to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainfreeattributeinfo(_:))*