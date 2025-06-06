# SecKeychainItemSetAccess(_:_:)

**Framework**: Security  
**Kind**: func

Sets the access of a given keychain item.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemSetAccess(_ itemRef: SecKeychainItem, _ access: SecAccess) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Use this function to attach an access instance to a particular keychain item. Alternatively, you can use the [`kSecAttrAccess`](ksecattraccess.md) attribute when calling either of the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) or [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md) methods.

## Parameters

- `itemRef`: A keychain item.
- `access`: An access instance to replace the keychain item’s current access instance. Use the   function to create a default access instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemsetaccess(_:_:))*