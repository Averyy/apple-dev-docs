# SecKeychainDelete(_:)

**Framework**: Security  
**Kind**: func

Deletes one or more keychains from the default keychain search list, and removes the keychain itself if it is a file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainDelete(_ keychainOrArray: SecKeychain?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). The result code [`errSecInvalidKeychain`](errsecinvalidkeychain.md) is returned if the specified keychain is invalid or if the value of the `keychainOrArray` parameter is invalid or `NULL`.

#### Discussion

The keychain may be a file stored locally, a smart card, or retrieved from a network server using non-file-based database protocols. This function deletes the keychain only if it is a local file.

This function does not release the memory used by the keychain object. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to release each keychain object when you are finished with it.

## Parameters

- `keychainOrArray`: In macOS 10.3 and later, passing   to this parameter returns an   error code. In OS X 10.2, this parameter was named   and only took a single keychain object. Passing   to this parameter deleted the user’s default keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaindelete(_:))*