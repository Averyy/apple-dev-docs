# SecKeychainItemCreateFromContent(_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a new keychain item from the supplied parameters.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafeRawPointer?, _ keychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Each item stored in the keychain contains data (such as a certificate), which is indexed by the item’s attributes. Use this function to create a keychain item from its attributes and data. To create keychain items that hold passwords, use the [`SecKeychainAddInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](seckeychainaddinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) or [`SecKeychainAddGenericPassword(_:_:_:_:_:_:_:_:)`](seckeychainaddgenericpassword(_:_:_:_:_:_:_:_:).md) functions.

A `SecKeychainItemRef` object for a certificate that is stored in a keychain can be safely cast to a `SecCertificateRef` for use with the Certificate, Key, and Trust API.

This function automatically calls the function [`SecKeychainUnlock(_:_:_:_:)`](seckeychainunlock(_:_:_:_:).md) to display the Unlock Keychain dialog box if the keychain is currently locked.

## Parameters

- `itemClass`: A constant identifying the class of item to create. See   for valid constants.
- `attrList`: A pointer to the list of attributes for the item to create.
- `length`: The length of the buffer pointed to by the   parameter.
- `data`: A pointer to a buffer containing the data to store.
- `keychainRef`: A reference to the keychain in which to add the item. Pass   to specify the default keychain.
- `initialAccess`: An access object for this keychain item. Use the   function to create an access object or the   function to copy an access object from another keychain item. If you pass   for this parameter, the access defaults to the application creating the item.
- `itemRef`: On return, a pointer to a reference to the newly created keychain item. This parameter is optional. You must call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemcreatefromcontent(_:_:_:_:_:_:_:))*