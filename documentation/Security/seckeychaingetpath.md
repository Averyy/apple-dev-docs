# SecKeychainGetPath(_:_:_:)

**Framework**: Security  
**Kind**: func

Determines the path of a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainGetPath(_ keychain: SecKeychain?, _ ioPathLength: UnsafeMutablePointer<UInt32>, _ pathName: UnsafeMutablePointer<CChar>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `keychain`: A reference to a keychain whose path you wish to obtain.
- `ioPathLength`: On return, the string length of  , not including the null termination.
- `pathName`: On entry, a pointer to a buffer that you have allocated. On return, the buffer contains POSIX path of the keychain as a null-terminated UTF-8 encoded string. The function returns   if the provided buffer is too small to hold the string with the null terminator byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetpath(_:_:_:))*