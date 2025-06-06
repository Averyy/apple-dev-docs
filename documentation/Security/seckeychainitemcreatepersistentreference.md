# SecKeychainItemCreatePersistentReference(_:_:)

**Framework**: Security  
**Kind**: func

Creates a persistent reference for a keychain item.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemCreatePersistentReference(_ itemRef: SecKeychainItem, _ persistentItemRef: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Unlike normal references, a persistent reference may be stored on disk or passed between processes. You can convert a persistent reference into an ordinary keychain item reference (`SecKeychainItemRef`) by calling the [`SecKeychainItemCopyFromPersistentReference(_:_:)`](seckeychainitemcopyfrompersistentreference(_:_:).md) function.

## Parameters

- `itemRef`: A keychain item reference for the item for which you want a persistent reference.
- `persistentItemRef`: On return, a persistent reference for the keychain item. You must call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcreatepersistentreference(_:_:))*