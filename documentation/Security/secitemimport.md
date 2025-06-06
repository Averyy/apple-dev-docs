# SecItemImport(_:_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Imports one or more certificates, keys, or identities and optionally adds them to a keychain.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecItemImport(_ importedData: CFData, _ fileNameOrExtension: CFString?, _ inputFormat: UnsafeMutablePointer<SecExternalFormat>?, _ itemType: UnsafeMutablePointer<SecExternalItemType>?, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>?, _ importKeychain: SecKeychain?, _ outItems: UnsafeMutablePointer<CFArray?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function uses the `fileNameOrExtension`, `inputFormat`, and `itemType` parameters to help it interpret the incoming data. In most cases, [`SecItemImport(_:_:_:_:_:_:_:_:)`](secitemimport(_:_:_:_:_:_:_:_:).md) can correctly interpret an external item if none of these are specified, but it is safer for you not to count on that ability.

When the output item type is [`SecExternalItemType.itemTypeAggregate`](secexternalitemtype/itemtypeaggregate.md), you can use the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFGetTypeID(_:)) function to determine the Core Foundation type of each item and the functions in `Getting Information About Keychain Services and Types` to determine the keychain item type of each item. For example, the following code determines whether the item is a certificate:

```objc
CFTypeID theID = CFGetTypeID(theItem);
if (SecCertificateGetTypeID() == theID)
```

You can pass in `NULL` for both `outItems` and `importKeychain` to determine what is inside a given external data representation. When you do, the function returns the input format and the item type without modifying the data in any way.

## Parameters

- `importedData`: A   object containing the data to import.
- `fileNameOrExtension`: Optional. The name of the file from which the external representation was previously read, or if that is unknown, then the file extension ( , for example). This serves as a hint for the key format and key type detection code.
- `inputFormat`: Pass   if you don’t know or don’t care what format the external representation is in.
- `itemType`: Pass   if you don’t know or don’t care what key type the external representation contains.
- `flags`: Note that PEM formatting is determined internally via inspection of the incoming data, so the   flag  is ignored.
- `keyParams`: A pointer to a structure containing a set of input parameters for the function. See  .
- `importKeychain`: Optional. The keychain into which the item should be imported. Pass   if you do not want to import the item into a keychain.
- `outItems`: Upon return, the referenced variable is overwritten by a new   array that contains   objects, each of which may be a  ,  , or   object. The caller is responsible for releasing this   object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimport(_:_:_:_:_:_:_:_:))*