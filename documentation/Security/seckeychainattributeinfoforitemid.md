# SecKeychainAttributeInfoForItemID(_:_:_:)

**Framework**: Security  
**Kind**: func

Obtains tags for all possible attributes of a given item class.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain?, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This call returns more attributes than are supported by the old style Keychain API and passing them into older calls yields an invalid attribute error. The recommended call to retrieve the attribute values is the [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](seckeychainitemcopyattributesanddata(_:_:_:_:_:_:).md) function.

> **Note**:  This is a CSSM-based API. CSSM is deprecated. For new development, where possible, you should generally use [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) to obtain the attributes of keychain items instead, because that function is based on Core Foundation types.

 This is a CSSM-based API. CSSM is deprecated.

For new development, where possible, you should generally use [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) to obtain the attributes of keychain items instead, because that function is based on Core Foundation types.

## Parameters

- `keychain`: A keychain object.
- `itemID`: The relation identifier of the item tags. An   is a   type as defined in  .
- `info`: On return, a pointer to the keychain attribute information. Your application should call the   function to release this structure when done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattributeinfoforitemid(_:_:_:))*