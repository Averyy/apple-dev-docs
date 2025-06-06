# SecKeychainItemCopyAccess(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the access of a given keychain item.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemCopyAccess(_ itemRef: SecKeychainItem, _ access: UnsafeMutablePointer<SecAccess?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Use this method to retrieve the access instance from a keychain item. Alternatively, you can look for the [`kSecAttrAccess`](ksecattraccess.md) attribute among the keychain item’s attributes when you call the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) method.

## Parameters

- `itemRef`: A keychain item.
- `access`: On return, points to the keychain item’s access instance. Call the   method to release this access instance when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcopyaccess(_:_:))*