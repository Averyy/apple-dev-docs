# SecKeychainItemFreeAttributesAndData(_:_:)

**Framework**: Security  
**Kind**: func

Releases the memory used by the keychain attribute list and/or the keychain data retrieved in a call to `SecKeychainItemCopyAttributesAndData`.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemFreeAttributesAndData(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ data: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `attrList`: A pointer to the attribute list to release. Pass   if there is no attribute list to release.
- `data`: A pointer to the data buffer to release. Pass   if there is no data to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemfreeattributesanddata(_:_:))*