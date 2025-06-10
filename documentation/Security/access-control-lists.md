# Access Control Lists

**Framework**: Security

Control which apps have access to keychain items in macOS.

#### Overview

In macOS, for items not stored on the iCloud keychain, each protected keychain item—like a password or private key—has an associated access instance that contains an access control list (ACL). The entries in this list in turn each contain an array of operations and an array of apps trusted to carry out those operations with the item. The collection of ACL entries govern the accessibility of the corresponding keychain item.

![Diagram showing the detailed contents of access attribute of a kechain item, namely an access control list composed of entries for different operations and trusted apps.](https://docs-assets.developer.apple.com/published/8c69c5a70381015d07af31a6c33c000a/media-2983146%402x.png)

When an app attempts to access a keychain item for a particular purpose—like using a private key to sign a document—the system looks for an entry in the item’s ACL containing the operation. If there’s no entry that lists the operation, then the system denies access and it’s up to the calling app to try something else or to notify the user.

If there is an entry that lists the operation, the system checks whether the calling app is among the entry’s trusted apps. If so, the system grants access. Otherwise, the system prompts the user for confirmation. The user may choose to Deny, Allow, or Always Allow the access. In the latter case, the system adds the app to the list of trusted apps for that entry, enabling the app to gain access in the future without prompting the user again.

> ❗ **Important**:  ACLs are not available in iOS or in macOS apps that use the iCloud keychain. For keychain item sharing in those environments, use access groups instead. See [`Sharing access to keychain items among a collection of apps`](sharing-access-to-keychain-items-among-a-collection-of-apps.md).

## Topics

### Access Creation
- [func SecAccessCreate(CFString, CFArray?, UnsafeMutablePointer<SecAccess?>) -> OSStatus](secaccesscreate(_:_:_:).md)
  Creates a new access instance associated with a given protected keychain item.
- [func SecAccessCreateWithOwnerAndACL(uid_t, gid_t, SecAccessOwnerType, CFArray?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccess?](secaccesscreatewithownerandacl(_:_:_:_:_:).md)
  Creates a new access instance using the owner and ACL entries you provide.
- [typealias SecAccessOwnerType](secaccessownertype.md)
  A type for flags that enable you to configure ACL ownership.
- [SecAccessOwnerType Values](secaccessownertype-values.md)
  Flags that enable you to configure ACL ownership.
- [class SecAccess](secaccess.md)
  An opaque type that identifies a keychain item’s access information.
- [func SecAccessGetTypeID() -> CFTypeID](secaccessgettypeid().md)
  Returns the unique identifier of the opaque type to which an access instance belongs.
### Access Query
- [func SecAccessCopyACLList(SecAccess, UnsafeMutablePointer<CFArray?>) -> OSStatus](secaccesscopyacllist(_:_:).md)
  Retrieves all the ACL entries of a given access instance.
- [func SecAccessCopyMatchingACLList(SecAccess, CFTypeRef) -> CFArray?](secaccesscopymatchingacllist(_:_:).md)
  Retrieves selected ACL entries from a given access instance.
- [func SecAccessCopyOwnerAndACL(SecAccess, UnsafeMutablePointer<uid_t>?, UnsafeMutablePointer<gid_t>?, UnsafeMutablePointer<SecAccessOwnerType>?, UnsafeMutablePointer<CFArray?>?) -> OSStatus](secaccesscopyownerandacl(_:_:_:_:_:).md)
  Retrieves the owner and the ACL entries of a given access instance.
### Access Control List Entries
- [func SecACLCreateWithSimpleContents(SecAccess, CFArray?, CFString, SecKeychainPromptSelector, UnsafeMutablePointer<SecACL?>) -> OSStatus](secaclcreatewithsimplecontents(_:_:_:_:_:).md)
  Creates a new ACL entry with the given characteristics, and adds it to an access instance.
- [func SecACLRemove(SecACL) -> OSStatus](secaclremove(_:).md)
  Removes the specified ACL entry from the access instance that contains it.
- [ACL Authorization Keys](acl-authorization-keys.md)
  The operations an access control list entry applies to.
- [struct SecKeychainPromptSelector](seckeychainpromptselector.md)
  Bits that define when a keychain should require a passphrase.
- [class SecACL](secacl.md)
  An opaque type that represents information about an ACL entry.
- [func SecACLGetTypeID() -> CFTypeID](secaclgettypeid().md)
  Returns the unique identifier of the opaque type to which an ACL entry belongs.
### Access Control List Configuration
- [func SecACLCopyContents(SecACL, UnsafeMutablePointer<CFArray?>, UnsafeMutablePointer<CFString?>, UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus](secaclcopycontents(_:_:_:_:).md)
  Returns the application list, description, and prompt selector for a given ACL entry.
- [func SecACLSetContents(SecACL, CFArray?, CFString, SecKeychainPromptSelector) -> OSStatus](secaclsetcontents(_:_:_:_:).md)
  Sets the application list, description, and prompt selector for a given ACL entry.
- [func SecACLCopyAuthorizations(SecACL) -> CFArray](secaclcopyauthorizations(_:).md)
  Retrieves the authorization tags of a given ACL entry.
- [func SecACLUpdateAuthorizations(SecACL, CFArray) -> OSStatus](secaclupdateauthorizations(_:_:).md)
  Sets the authorization tags for a given ACL.
### Trusted Applications
- [func SecTrustedApplicationCreateFromPath(UnsafePointer<CChar>?, UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus](sectrustedapplicationcreatefrompath(_:_:).md)
  Creates a trusted app instance based on the app at the given path in the file system.
- [func SecTrustedApplicationCopyData(SecTrustedApplication, UnsafeMutablePointer<CFData?>) -> OSStatus](sectrustedapplicationcopydata(_:_:).md)
  Retrieves the data of a trusted app instance.
- [func SecTrustedApplicationSetData(SecTrustedApplication, CFData) -> OSStatus](sectrustedapplicationsetdata(_:_:).md)
  Sets the data of a given trusted app instance.
- [class SecTrustedApplication](sectrustedapplication.md)
  An opaque type that contains information about a trusted app.
- [func SecTrustedApplicationGetTypeID() -> CFTypeID](sectrustedapplicationgettypeid().md)
  Returns the unique identifier of the opaque type to which a trusted app instance belongs.
### Keychain Item Access
- [func SecKeychainItemSetAccess(SecKeychainItem, SecAccess) -> OSStatus](seckeychainitemsetaccess(_:_:).md)
  Sets the access of a given keychain item.
- [func SecKeychainItemCopyAccess(SecKeychainItem, UnsafeMutablePointer<SecAccess?>) -> OSStatus](seckeychainitemcopyaccess(_:_:).md)
  Retrieves the access of a given keychain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/access-control-lists)*