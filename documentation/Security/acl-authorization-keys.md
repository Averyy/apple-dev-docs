# ACL Authorization Keys

**Framework**: Security

The operations an access control list entry applies to.

## Topics

### Constants
- [let kSecACLAuthorizationAny: CFString](ksecaclauthorizationany.md)
  No restrictions. This ACL entry applies to all operations available to the caller.
- [let kSecACLAuthorizationLogin: CFString](ksecaclauthorizationlogin.md)
  Use for a CSP (smart card) login.
- [let kSecACLAuthorizationGenKey: CFString](ksecaclauthorizationgenkey.md)
  Generate a key.
- [let kSecACLAuthorizationDelete: CFString](ksecaclauthorizationdelete.md)
  Delete this item.
- [let kSecACLAuthorizationExportWrapped: CFString](ksecaclauthorizationexportwrapped.md)
  Export a wrapped (that is, encrypted) key. This tag is checked on the key being exported; in addition, the `CSSM_ACL_AUTHORIZATION_ENCRYPT` tag is checked for any key used in the wrapping operation.
- [let kSecACLAuthorizationExportClear: CFString](ksecaclauthorizationexportclear.md)
  Export an unencrypted key.
- [let kSecACLAuthorizationImportWrapped: CFString](ksecaclauthorizationimportwrapped.md)
  Import an encrypted key. This tag is checked on the key being imported; in addition, the `CSSM_ACL_AUTHORIZATION_DECRYPT` tag is checked for any key used in the unwrapping operation.
- [let kSecACLAuthorizationImportClear: CFString](ksecaclauthorizationimportclear.md)
  Import an unencrypted key.
- [let kSecACLAuthorizationSign: CFString](ksecaclauthorizationsign.md)
  Digitally sign data.
- [let kSecACLAuthorizationEncrypt: CFString](ksecaclauthorizationencrypt.md)
  Encrypt data.
- [let kSecACLAuthorizationDecrypt: CFString](ksecaclauthorizationdecrypt.md)
  Decrypt data.
- [let kSecACLAuthorizationMAC: CFString](ksecaclauthorizationmac.md)
  Create or verify a message authentication code.
- [let kSecACLAuthorizationDerive: CFString](ksecaclauthorizationderive.md)
  Derive a new key from another key.
- [let kSecACLAuthorizationKeychainCreate: CFString](ksecaclauthorizationkeychaincreate.md)
  Create a new keychain.
- [let kSecACLAuthorizationKeychainDelete: CFString](ksecaclauthorizationkeychaindelete.md)
  Delete a keychain.
- [let kSecACLAuthorizationKeychainItemRead: CFString](ksecaclauthorizationkeychainitemread.md)
  Read an item from a keychain.
- [let kSecACLAuthorizationKeychainItemInsert: CFString](ksecaclauthorizationkeychainiteminsert.md)
  Insert an item into a keychain.
- [let kSecACLAuthorizationKeychainItemModify: CFString](ksecaclauthorizationkeychainitemmodify.md)
  Modify an item in a keychain.
- [let kSecACLAuthorizationKeychainItemDelete: CFString](ksecaclauthorizationkeychainitemdelete.md)
  Delete an item from a keychain.
- [let kSecACLAuthorizationChangeACL: CFString](ksecaclauthorizationchangeacl.md)
  Change an access control list entry.
- [let kSecACLAuthorizationChangeOwner: CFString](ksecaclauthorizationchangeowner.md)
  For internal system use only. Use the `CSSM_ACL_AUTHORIZATION_CHANGE_ACL` tag for changes to owner ACL entries.
- [let kSecACLAuthorizationIntegrity: CFString](ksecaclauthorizationintegrity.md)
- [let kSecACLAuthorizationPartitionID: CFString](ksecaclauthorizationpartitionid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/acl-authorization-keys)*