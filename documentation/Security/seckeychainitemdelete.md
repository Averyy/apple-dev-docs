# SecKeychainItemDelete(_:)

**Framework**: Security  
**Kind**: func

Deletes a keychain item from the default keychain’s permanent data store.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemDelete(_ itemRef: SecKeychainItem) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If the keychain item has not previously been added to the keychain, this function does nothing and returns `noErr`.

Do not delete a keychain item and recreate it in order to modify it; instead, use the [`SecKeychainItemModifyContent(_:_:_:_:)`](seckeychainitemmodifycontent(_:_:_:_:).md) or [`SecKeychainItemModifyAttributesAndData(_:_:_:_:)`](seckeychainitemmodifyattributesanddata(_:_:_:_:).md) function to modify an existing keychain item. When you delete a keychain item, you lose any access controls and trust settings added by the user or by other applications.

## Parameters

- `itemRef`: A keychain item object of the item to delete. You must call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemdelete(_:))*