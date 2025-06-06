# SecKeychainItemFreeContent(_:_:)

**Framework**: Security  
**Kind**: func

Releases the memory used by the keychain attribute list and the keychain data retrieved in a call to the [`SecKeychainItemCopyContent(_:_:_:_:_:)`](seckeychainitemcopycontent(_:_:_:_:_:).md) function.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainItemFreeContent(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ data: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Because the [`SecKeychainFindInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](seckeychainfindinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) and [`SecKeychainFindGenericPassword(_:_:_:_:_:_:_:_:)`](seckeychainfindgenericpassword(_:_:_:_:_:_:_:_:).md) functions call the [`SecKeychainItemCopyContent(_:_:_:_:_:)`](seckeychainitemcopycontent(_:_:_:_:_:).md) function, you must call `SecKeychainItemFreeContent` to release the data buffers after calls to those functions as well.

Because the `SecKeychainItemCopyContent` function does not allocate buffers until they are needed, you should not call the `SecKeychainItemFreeContent` function unless data is actually returned to you.

## Parameters

- `attrList`: A pointer to the attribute list to release. Pass   if there is no attribute list to release.
- `data`: A pointer to the data buffer to release. Pass   if there is no data to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemfreecontent(_:_:))*