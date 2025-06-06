# Item class keys and values

**Framework**: Security

Specify the class of a keychain item.

#### Overview

Keychain items come in a variety of classes according to the kind of data they hold, such as passwords, cryptographic keys, and certificates. The item’s class dictates which attributes apply and enables the system to decide whether to encrypt the data. For example, the system encrypts passwords, but not certificates because they aren’t secret.

Use the key and one of the corresponding values listed here to specify the class for a new item you create with a call to the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function by placing the key/value pair in the `attributes` dictionary.

Later, use this same pair in the `query` dictionary when searching for an item with one of the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md), [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md), or [`SecItemDelete(_:)`](secitemdelete(_:).md) functions.

## Topics

### Item class keys
- [let kSecClass: CFString](ksecclass.md)
  A dictionary key whose value is the item’s class.
### Item class values
- [let kSecClassGenericPassword: CFString](ksecclassgenericpassword.md)
  The value that indicates a generic password item.
- [let kSecClassInternetPassword: CFString](ksecclassinternetpassword.md)
  The value that indicates an Internet password item.
- [let kSecClassCertificate: CFString](ksecclasscertificate.md)
  The value that indicates a certificate item.
- [let kSecClassKey: CFString](ksecclasskey.md)
  The value that indicates a cryptographic key item.
- [let kSecClassIdentity: CFString](ksecclassidentity.md)
  The value that indicates an identity item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/item-class-keys-and-values)*