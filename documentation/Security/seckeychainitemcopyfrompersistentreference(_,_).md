# SecKeychainItemCopyFromPersistentReference(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Provides a keychain item reference, given a persistent reference.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainItemCopyFromPersistentReference(_ persistentItemRef: CFData, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus
```

```c
OSStatus SecKeychainItemCopyFromPersistentReference(CFDataRef persistentItemRef, SecKeychainItemRef*itemRef);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

A persistent reference may be stored on disk or passed between processes. You use the [`SecKeychainItemCreatePersistentReference(_:_:)`](./seckeychainitemcreatepersistentreference%28_,_%29.md) function to create a persistent reference.

## Parameters

- `persistentItemRef`: A persistent reference for a keychain item.
- `itemRef`: On return, a keychain item reference for the item for which you provided a persistent reference. You must call the `CFRelease` function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcopyfrompersistentreference(_:_:))*