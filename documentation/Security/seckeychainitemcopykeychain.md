# SecKeychainItemCopyKeychain(_:_:)

**Framework**: Security  
**Kind**: func

Returns the keychain object of a given keychain item.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemCopyKeychain(_ itemRef: SecKeychainItem, _ keychainRef: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `itemRef`: A keychain item object.
- `keychainRef`: On return, a pointer to a keychain object referencing the given keychain item. You must call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcopykeychain(_:_:))*