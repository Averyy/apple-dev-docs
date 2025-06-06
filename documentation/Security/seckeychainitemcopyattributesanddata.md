# SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the data and/or attributes stored in the given keychain item.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem, _ info: UnsafeMutablePointer<SecKeychainAttributeInfo>?, _ itemClass: UnsafeMutablePointer<SecItemClass>?, _ attrList: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>?>?, _ length: UnsafeMutablePointer<UInt32>?, _ outData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function returns the data and attributes of a specific keychain item.

> **Note**:  This is a CSSM-based API. CSSM is deprecated. For new development, where possible, you should generally use [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) to obtain attributes of keychain items instead, because that function is based on Core Foundation types.

You can use the [`SecKeychainSearchCopyNext`](seckeychainsearchcopynext.md) function to search for a keychain item if you don’t already have the item’s reference object. To find and obtain data from a password keychain item, use the [`SecKeychainFindInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](seckeychainfindinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) or [`SecKeychainFindGenericPassword(_:_:_:_:_:_:_:_:)`](seckeychainfindgenericpassword(_:_:_:_:_:_:_:_:).md) function.

You should pair the `SecKeychainItemCopyAttributesAndData` function with the [`SecKeychainItemModifyAttributesAndData(_:_:_:_:)`](seckeychainitemmodifyattributesanddata(_:_:_:_:).md) function, as these functions handle more attributes than are support by the old Keychain Manager and passing them into older calls yields an invalid attribute error. Use the functions [`SecKeychainItemModifyContent(_:_:_:_:)`](seckeychainitemmodifycontent(_:_:_:_:).md) and [`SecKeychainItemCopyContent(_:_:_:_:_:)`](seckeychainitemcopycontent(_:_:_:_:_:).md) when dealing with older Keychain Manager functions.

If the keychain item data is encrypted, this function decrypts the data before returning it to you. If the calling application is not in the list of trusted applications, the user is prompted before access is allowed. If the access controls for this item do not allow decryption, the function returns the `errSecAuthFailed` result code.

## Parameters

- `itemRef`: A reference to the keychain item from which you wish to retrieve data or attributes.
- `info`: A pointer to a list of tags and formats of attributes to retrieve. You can call   to obtain a list of all possible attribute tags and formats for the item’s class. Pass   if you don’t wish to retrieve any attributes.
- `itemClass`: On return, the item’s class. Pass   if not required. See   for valid constants.
- `attrList`: On return, the retrieved attributes and their values .  Pass   if not required. You must call the function   when you no longer need the attributes and values.
- `length`: On return, the actual length of the data returned in the   parameter.
- `outData`: On return, the data in this item. Pass   if not required. You must call the function   when you no longer need the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcopyattributesanddata(_:_:_:_:_:_:))*