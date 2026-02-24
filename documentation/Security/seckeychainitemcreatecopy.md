# SecKeychainItemCreateCopy(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Copies a keychain item from one keychain to another.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem, _ destKeychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemCopy: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `itemRef`: A reference to the keychain item to copy.
- `destKeychainRef`: A reference to the keychain in which to insert the copied keychain item. Pass `NULL` to specify the default keychain.
- `initialAccess`: The initial access for the copied keychain item. Use the [`SecAccessCreate(_:_:_:)`](secaccesscreate(_:_:_:).md) function to create an access object or the [`SecKeychainItemCopyAccess(_:_:)`](seckeychainitemcopyaccess(_:_:).md) function to copy an access object from another keychain item. If you pass `NULL` for this parameter, the access defaults to the application creating the item.
- `itemCopy`: On return, a pointer to a copy of the keychain item referenced by the `itemRef` parameter. You must call the `CFRelease` function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcreatecopy(_:_:_:_:))*