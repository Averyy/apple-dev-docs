# Item return result keys

**Framework**: Security

Specify how you want returned keychain item data formatted.

#### Overview

When you use one of the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) or [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) functions to add or search for keychain items, these functions return the item’s data and attributes through the `result` parameter to which you provide a pointer. Use the item result keys described below in the corresponding query dictionary to indicate how those results should be formatted:

- If you request a data reference with [`kSecReturnRef`](ksecreturnref.md), the search returns a reference of type [`SecKeychainItem`](seckeychainitem.md), [`SecKey`](seckey.md), [`SecCertificate`](seccertificate.md), [`SecIdentity`](secidentity.md), or doc://com.apple.documentation/documentation/corefoundation/cfdata-rv9, depending on the class of the item.
- If you request a persistent data reference using [`kSecReturnPersistentRef`](ksecreturnpersistentref.md), the search returns an item reference of type doc://com.apple.documentation/documentation/corefoundation/cfdata-rv9 that you can store on disk or pass between processes. You later convert persistent references to regular references with another call to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function, using an array of persistent references (of the same item class) as the value for the [`kSecMatchItemList`](ksecmatchitemlist.md) key.
- If you ask for the data itself with [`kSecReturnData`](ksecreturndata.md), the search returns a doc://com.apple.documentation/documentation/corefoundation/cfdata-rv9 instance that holds the actual data. This is typically what you want for password items. To undo the encryption it added prior to storing the item, keychain services decrypts the data before returning it to you. Don’t use [`kSecReturnData`](ksecreturndata.md) for cryptographic key or identity items, as the key material may not be extractable. Instead, call [`SecKeyCopyExternalRepresentation(_:_:)`](seckeycopyexternalrepresentation(_:_:).md), and check the `error` parameter if it returns `nil`.
- If you request the item’s attributes using [`kSecReturnAttributes`](ksecreturnattributes.md) or more than one return type, the search returns a dictionary. Item attributes are represented directly as key-value pairs in this dictionary, while the item’s data appears in one or more of the previously mentioned forms, and is associated with the appropriate item value type key from [`Item return result keys`](item-return-result-keys.md).
- When you specify a match limit greater than one, the search produces an array. Each element of the array is itself a search result formatted according to the previous rules.

## Topics

### Item result keys
- [let kSecReturnData: CFString](ksecreturndata.md)
  A key whose value is a Boolean that indicates whether or not to return item data.
- [let kSecReturnAttributes: CFString](ksecreturnattributes.md)
  A key whose value is a Boolean indicating whether or not to return item attributes.
- [let kSecReturnRef: CFString](ksecreturnref.md)
  A key whose value is a Boolean indicating whether or not to return a reference to an item.
- [let kSecReturnPersistentRef: CFString](ksecreturnpersistentref.md)
  A key whose value is a Boolean indicating whether or not to return a persistent reference to an item.
### Item value type keys
- [let kSecValueData: CFString](ksecvaluedata.md)
  A key whose value is the item’s data.
- [let kSecValueRef: CFString](ksecvalueref.md)
  A key whose value is a reference to the item.
- [let kSecValuePersistentRef: CFString](ksecvaluepersistentref.md)
  A key whose value is a persistent reference to the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/item-return-result-keys)*