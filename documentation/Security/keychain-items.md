# Keychain items

**Framework**: Security

Embed confidential information in items that you store in a keychain.

#### Overview

When you want to store a secret such as a password or cryptographic key, you package it as a keychain item. Along with the data itself, you provide a set of publicly visible attributes both to control the item’s accessibility and to make it searchable. As shown in Figure 1, keychain services handles data encryption and storage (including data attributes) in a keychain, which is an encrypted database stored on disk. Later, authorized processes use keychain services to find the item and decrypt its data.

![Diagram showing data being encrypted and then combined with attributes into a keychain item before being stored in a keychain.](https://docs-assets.developer.apple.com/published/192ae065b3c41c60bff42cbf95f0d33c/media-2891903%402x.png)

## Topics

### Essentials
- [Using the keychain to manage user secrets](using-the-keychain-to-manage-user-secrets.md)
  Relieve the user of remembering small secrets by storing them in the keychain.
- [TN3137: On Mac keychain APIs and implementations](../Technotes/tn3137-on-mac-keychains.md)
  Learn how the keychain on macOS differs from other Apple platforms.
- [class SecKeychainItem](seckeychainitem.md)
  An opaque type that represents a keychain item.
- [func SecKeychainItemGetTypeID() -> CFTypeID](seckeychainitemgettypeid().md)
  Returns the unique identifier of the opaque type to which a keychain item object belongs.
### Adding keychain items
- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)
  Add network credentials to the keychain on behalf of the user.
- [func SecItemAdd(CFDictionary, UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus](secitemadd(_:_:).md)
  Adds one or more items to a keychain.
- [Item class keys and values](item-class-keys-and-values.md)
  Specify the class of a keychain item.
- [Item attribute keys and values](item-attribute-keys-and-values.md)
  Specify the attributes of keychain items.
### Keychain item search
- [Searching for keychain items](searching-for-keychain-items.md)
  Find keychain items based on search criteria that you specify.
- [func SecItemCopyMatching(CFDictionary, UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus](secitemcopymatching(_:_:).md)
  Returns one or more keychain items that match a search query, or copies attributes of specific keychain items.
- [Search attribute keys and values](search-attribute-keys-and-values.md)
  Filter a keychain item search.
- [Item return result keys](item-return-result-keys.md)
  Specify how you want returned keychain item data formatted.
### Keychain item modification
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)
  Modify items in the keychain when the user’s data changes.
- [func SecItemUpdate(CFDictionary, CFDictionary) -> OSStatus](secitemupdate(_:_:).md)
  Modifies items that match a search query.
- [func SecItemDelete(CFDictionary) -> OSStatus](secitemdelete(_:).md)
  Deletes items that match a search query.
### Keychain item access
- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)
  Enable apps to share keychain items with each other by adding the apps to an access group.
- [Keychain Access Groups Entitlement](../BundleResources/Entitlements/keychain-access-groups.md)
  The identifiers for the keychain groups that the app may share items with.
- [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md)
  Set the conditions under which an app can access a keychain item such as a password.
- [func SecAccessControlCreateWithFlags(CFAllocator?, CFTypeRef, SecAccessControlCreateFlags, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccessControl?](secaccesscontrolcreatewithflags(_:_:_:_:).md)
  Creates a new access control object with the specified protection type and flags.
- [struct SecAccessControlCreateFlags](secaccesscontrolcreateflags.md)
  Access control constants that dictate how a keychain item may be used.
- [class SecAccessControl](secaccesscontrol.md)
  An opaque type that contains information about how a keychain item may be used.
- [func SecAccessControlGetTypeID() -> CFTypeID](secaccesscontrolgettypeid().md)
  Returns the unique identifier of the opaque type to which a keychain item access control object belongs.
### Import and export
- [func SecItemImport(CFData, CFString?, UnsafeMutablePointer<SecExternalFormat>?, UnsafeMutablePointer<SecExternalItemType>?, SecItemImportExportFlags, UnsafePointer<SecItemImportExportKeyParameters>?, SecKeychain?, UnsafeMutablePointer<CFArray?>?) -> OSStatus](secitemimport(_:_:_:_:_:_:_:_:).md)
  Imports one or more certificates, keys, or identities and optionally adds them to a keychain.
- [func SecItemExport(CFTypeRef, SecExternalFormat, SecItemImportExportFlags, UnsafePointer<SecItemImportExportKeyParameters>?, UnsafeMutablePointer<CFData?>) -> OSStatus](secitemexport(_:_:_:_:_:).md)
  Exports one or more certificates, keys, or identities.
- [enum SecExternalFormat](secexternalformat.md)
  The external format of a keychain item.
- [enum SecExternalItemType](secexternalitemtype.md)
  The import item type.
- [struct SecItemImportExportFlags](secitemimportexportflags.md)
  The import and export function flags.
- [struct SecItemImportExportKeyParameters](secitemimportexportkeyparameters.md)
  The import/export parameter structure.
- [struct SecKeyImportExportFlags](seckeyimportexportflags.md)
  The import/export parameter structure flags.
- [var SEC_KEY_IMPORT_EXPORT_PARAMS_VERSION: Int32](sec_key_import_export_params_version.md)
  The import/export parameter structure version.
- [struct SecKeyImportExportParameters](seckeyimportexportparameters.md)
  The legacy import/export parameter structure.
### Legacy keychain item creation
- [func SecKeychainItemCreateFromContent(SecItemClass, UnsafeMutablePointer<SecKeychainAttributeList>, UInt32, UnsafeRawPointer?, SecKeychain?, SecAccess?, UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](seckeychainitemcreatefromcontent(_:_:_:_:_:_:_:).md)
  Creates a new keychain item from the supplied parameters.
- [func SecKeychainItemCreateCopy(SecKeychainItem, SecKeychain?, SecAccess?, UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](seckeychainitemcreatecopy(_:_:_:_:).md)
  Copies a keychain item from one keychain to another.
- [func SecKeychainItemCreatePersistentReference(SecKeychainItem, UnsafeMutablePointer<CFData?>) -> OSStatus](seckeychainitemcreatepersistentreference(_:_:).md)
  Creates a persistent reference for a keychain item.
- [func SecKeychainItemCopyFromPersistentReference(CFData, UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](seckeychainitemcopyfrompersistentreference(_:_:).md)
  Provides a keychain item reference, given a persistent reference.
- [enum SecItemClass](secitemclass.md)
  Specifies a keychain item’s class code.
### Legacy keychain item management
- [func SecKeychainItemCopyAttributesAndData(SecKeychainItem, UnsafeMutablePointer<SecKeychainAttributeInfo>?, UnsafeMutablePointer<SecItemClass>?, UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>?>?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus](seckeychainitemcopyattributesanddata(_:_:_:_:_:_:).md)
  Retrieves the data and/or attributes stored in the given keychain item.
- [func SecKeychainItemModifyAttributesAndData(SecKeychainItem, UnsafePointer<SecKeychainAttributeList>?, UInt32, UnsafeRawPointer?) -> OSStatus](seckeychainitemmodifyattributesanddata(_:_:_:_:).md)
  Updates an existing keychain item after changing its attributes or data.
- [func SecKeychainItemFreeAttributesAndData(UnsafeMutablePointer<SecKeychainAttributeList>?, UnsafeMutableRawPointer?) -> OSStatus](seckeychainitemfreeattributesanddata(_:_:).md)
  Releases the memory used by the keychain attribute list and/or the keychain data retrieved in a call to `SecKeychainItemCopyAttributesAndData`.
- [func SecKeychainItemCopyContent(SecKeychainItem, UnsafeMutablePointer<SecItemClass>?, UnsafeMutablePointer<SecKeychainAttributeList>?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus](seckeychainitemcopycontent(_:_:_:_:_:).md)
  Copies the data and attributes stored in the given keychain item.
- [func SecKeychainItemModifyContent(SecKeychainItem, UnsafePointer<SecKeychainAttributeList>?, UInt32, UnsafeRawPointer?) -> OSStatus](seckeychainitemmodifycontent(_:_:_:_:).md)
  Updates an existing keychain item after changing its attributes and/or data.
- [func SecKeychainItemFreeContent(UnsafeMutablePointer<SecKeychainAttributeList>?, UnsafeMutableRawPointer?) -> OSStatus](seckeychainitemfreecontent(_:_:).md)
  Releases the memory used by the keychain attribute list and the keychain data retrieved in a call to the [`SecKeychainItemCopyContent(_:_:_:_:_:)`](seckeychainitemcopycontent(_:_:_:_:_:).md) function.
- [func SecKeychainItemCopyKeychain(SecKeychainItem, UnsafeMutablePointer<SecKeychain?>) -> OSStatus](seckeychainitemcopykeychain(_:_:).md)
  Returns the keychain object of a given keychain item.
- [func SecKeychainItemDelete(SecKeychainItem) -> OSStatus](seckeychainitemdelete(_:).md)
  Deletes a keychain item from the default keychain’s permanent data store.
- [typealias SecKeychainAttrType](seckeychainattrtype.md)
  The keychain attribute type.
- [struct SecKeychainAttribute](seckeychainattribute.md)
  A structure that holds a single keychain attribute.
- [typealias SecKeychainAttributePtr](seckeychainattributeptr.md)
  A pointer to a keychain attribute structure.
- [struct SecKeychainAttributeList](seckeychainattributelist.md)
  A list of keychain attributes.
### Legacy attribute info
- [func SecKeychainAttributeInfoForItemID(SecKeychain?, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>?>) -> OSStatus](seckeychainattributeinfoforitemid(_:_:_:).md)
  Obtains tags for all possible attributes of a given item class.
- [func SecKeychainFreeAttributeInfo(UnsafeMutablePointer<SecKeychainAttributeInfo>) -> OSStatus](seckeychainfreeattributeinfo(_:).md)
  Releases the memory acquired by calling the `SecKeychainAttributeInfoForItemID` function.
- [struct SecKeychainAttributeInfo](seckeychainattributeinfo.md)
  A structure that represents an attribute.
- [enum SecItemAttr](secitemattr.md)
  Specifies a keychain item’s attributes.
- [Keychain Item Attribute Constants For Keys](keychain-item-attribute-constants-for-keys.md)
  Specifies the attributes for a key item in a keychain.
- [typealias SecAFPServerSignature](secafpserversignature.md)
  Represents a 16-byte Apple File Protocol server signature block.
### Legacy password storage
- [func SecKeychainAddInternetPassword(SecKeychain?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UInt16, SecProtocolType, SecAuthenticationType, UInt32, UnsafeRawPointer, UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](seckeychainaddinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Adds a new Internet password to a keychain.
- [func SecKeychainFindInternetPassword(CFTypeRef?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UInt16, SecProtocolType, SecAuthenticationType, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](seckeychainfindinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Finds the first Internet password based on the attributes passed.
- [func SecKeychainAddGenericPassword(SecKeychain?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafeRawPointer, UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](seckeychainaddgenericpassword(_:_:_:_:_:_:_:_:).md)
  Adds a new generic password to a keychain.
- [func SecKeychainFindGenericPassword(CFTypeRef?, UInt32, UnsafePointer<CChar>?, UInt32, UnsafePointer<CChar>?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](seckeychainfindgenericpassword(_:_:_:_:_:_:_:_:).md)
  Finds the first generic password based on the attributes passed.
- [enum SecProtocolType](secprotocoltype.md)
  The protocol type associated with an Internet password.
- [enum SecAuthenticationType](secauthenticationtype.md)
  The authentication type to use for an Internet password.
- [class SecPassword](secpassword.md)
  Contains information about a password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/keychain-items)*