# SecKeychainItemModifyAttributesAndData(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Updates an existing keychain item after changing its attributes or data.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>?, _ length: UInt32, _ data: UnsafeRawPointer?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The keychain item is written to the keychain’s permanent data store. If the keychain item has not previously been added to a keychain, a call to this function does nothing and returns `noErr`.

> **Note**:  For new development, where possible, you should generally use [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md) to obtain attributes of keychain items instead, because that function is based on Core Foundation types.

 For new development, where possible, you should generally use [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md) to obtain attributes of keychain items instead, because that function is based on Core Foundation types.

Note that when you use this function to modify a keychain item, Keychain Services updates the modification date of the item. Therefore, you cannot use this function to modify the modification date, as the value you specify will be overwritten with the current time. If you want to change the modification date to something other than the current time, use a CSSM function to do so.

You should pair the [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](seckeychainitemcopyattributesanddata(_:_:_:_:_:_:).md) function with the `SecKeychainItemModifyAttributesAndData` function, as these functions handle more attributes than are support by the old Keychain Manager and passing them into older calls yields an invalid attribute error. Use the functions [`SecKeychainItemModifyContent(_:_:_:_:)`](seckeychainitemmodifycontent(_:_:_:_:).md) and [`SecKeychainItemCopyContent(_:_:_:_:_:)`](seckeychainitemcopycontent(_:_:_:_:_:).md) when dealing with older Keychain Manager functions.

## Parameters

- `itemRef`: A reference to the keychain item to modify.
- `attrList`: A pointer to the list of attributes to modify and their new values. Pass   if you have no need to modify attributes.
- `length`: The length of the buffer pointed to by the   parameter. Pass   if you pass   in the   parameter.
- `data`: A pointer to a buffer containing the data to store. Pass   if you do not need to modify the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemmodifyattributesanddata(_:_:_:_:))*