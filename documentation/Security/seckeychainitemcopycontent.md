# SecKeychainItemCopyContent(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Copies the data and attributes stored in the given keychain item.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem, _ itemClass: UnsafeMutablePointer<SecItemClass>?, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ length: UnsafeMutablePointer<UInt32>?, _ outData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function returns the data and attributes of a specific keychain item.

> **Note**:  For new development, where possible, you should generally use [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) to obtain the data and attributes of keychain items instead, because that function is based on Core Foundation types.

 For new development, where possible, you should generally use [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) to obtain the data and attributes of keychain items instead, because that function is based on Core Foundation types.

You can use the [`SecKeychainSearchCopyNext`](seckeychainsearchcopynext.md) function to search for a keychain item if you don’t already have the item’s reference object. To find and obtain data from a password keychain item, use the [`SecKeychainFindInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](seckeychainfindinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) or [`SecKeychainFindGenericPassword(_:_:_:_:_:_:_:_:)`](seckeychainfindgenericpassword(_:_:_:_:_:_:_:_:).md) function.

You should pair the [`SecKeychainItemModifyContent(_:_:_:_:)`](seckeychainitemmodifycontent(_:_:_:_:).md) function with the `SecKeychainItemCopyContent` function when dealing with older Keychain Manager functions. The [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](seckeychainitemcopyattributesanddata(_:_:_:_:_:_:).md) and [`SecKeychainItemModifyAttributesAndData(_:_:_:_:)`](seckeychainitemmodifyattributesanddata(_:_:_:_:).md) functions handle more attributes than are supported by the old Keychain Manager; however, passing them into older calls yields an invalid attribute error.

If the keychain item data is encrypted, this function decrypts the data before returning it to you. If the calling application is not in the list of trusted applications, the user is prompted before access is allowed. If the access controls for this item do not allow decryption, the function returns the `errSecAuthFailed` result code.

## Parameters

- `itemRef`: A reference to the keychain item to modify.
- `itemClass`: On return, points to the item’s class. Pass   if it is not required. See   for valid constants.
- `attrList`: On entry, the list of attributes to get in this item; on return the attributes are filled in. Pass   if you don’t need to retrieve any attributes. You must call   when you no longer need the attributes and data.
- `length`: On return, the length of the buffer pointed to by the   parameter.
- `outData`: On return, a pointer to a buffer containing the data in this item. Pass   if you don’t need this data. You must call   when you no longer need the attributes and data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcopycontent(_:_:_:_:_:))*