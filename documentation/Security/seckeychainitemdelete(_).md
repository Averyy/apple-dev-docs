# SecKeychainItemDelete(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Deletes a keychain item from the default keychain’s permanent data store.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainItemDelete(_ itemRef: SecKeychainItem) -> OSStatus
```

```c
OSStatus SecKeychainItemDelete(SecKeychainItemRef itemRef);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

If the keychain item has not previously been added to the keychain, this function does nothing and returns `noErr`.

Do not delete a keychain item and recreate it in order to modify it; instead, use the [`SecKeychainItemModifyContent(_:_:_:_:)`](./seckeychainitemmodifycontent%28_,_,_,_%29.md) or [`SecKeychainItemModifyAttributesAndData(_:_:_:_:)`](./seckeychainitemmodifyattributesanddata%28_,_,_,_%29.md) function to modify an existing keychain item. When you delete a keychain item, you lose any access controls and trust settings added by the user or by other applications.

## Parameters

- `itemRef`: A keychain item object of the item to delete. You must call the `CFRelease` function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemdelete(_:))*