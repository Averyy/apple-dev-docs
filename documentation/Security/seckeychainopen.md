# SecKeychainOpen(_:_:)

**Framework**: Security  
**Kind**: func

Opens a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainOpen(_ pathName: UnsafePointer<CChar>, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Use this function to retrieve a pointer to a keychain object given the path of the keychain. You don’t need to close the keychain, but do release the memory that the pointer occupies when you are finished with it.

## Parameters

- `pathName`: A constant character string representing the POSIX path to the keychain to open.
- `keychain`: On return, a pointer to the keychain object. You must call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainopen(_:_:))*