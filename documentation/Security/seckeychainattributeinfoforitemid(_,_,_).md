# SecKeychainAttributeInfoForItemID(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains tags for all possible attributes of a given item class.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain?, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>?>) -> OSStatus
```

```c
OSStatus SecKeychainAttributeInfoForItemID(SecKeychainRef keychain, UInt32 itemID, SecKeychainAttributeInfo **info);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

This call returns more attributes than are supported by the old style Keychain API and passing them into older calls yields an invalid attribute error. The recommended call to retrieve the attribute values is the [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](./seckeychainitemcopyattributesanddata%28_,_,_,_,_,_%29.md) function.

> **Note**:  This is a CSSM-based API. CSSM is deprecated.
>
> For new development, where possible, you should generally use [`SecItemCopyMatching(_:_:)`](./secitemcopymatching%28_,_%29.md) to obtain the attributes of keychain items instead, because that function is based on Core Foundation types.

## Parameters

- `keychain`: A keychain object.
- `itemID`: The relation identifier of the item tags. An `itemID` is a `CSSM_DB_RECORDTYPE` type as defined in `cssmtype.h`.
- `info`: On return, a pointer to the keychain attribute information. Your application should call the [`SecKeychainFreeAttributeInfo(_:)`](./seckeychainfreeattributeinfo%28_%29.md) function to release this structure when done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattributeinfoforitemid(_:_:_:))*