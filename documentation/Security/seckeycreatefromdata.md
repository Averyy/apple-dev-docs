# SecKeyCreateFromData(_:_:_:)

**Framework**: Security  
**Kind**: func

Constructs a SecKeyRef object for a symmetric key.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyCreateFromData(_ parameters: CFDictionary, _ keyData: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

#### Return Value

A symmetric key. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free the key’s memory when you are done with it.

#### Discussion

The parameters dictionary must contain (at minimum) an entry for the [`kSecAttrKeyType`](ksecattrkeytype.md) key with a value of [`kSecAttrKeyTypeAES`](ksecattrkeytypeaes.md) or any other key type defined in Key Type Value.

The keys below may be optionally set in the parameters dictionary (with a `CFBooleanRef` value) to override the default key usage values:

- [`kSecAttrCanEncrypt`](ksecattrcanencrypt.md)
- [`kSecAttrCanDecrypt`](ksecattrcandecrypt.md)
- [`kSecAttrCanWrap`](ksecattrcanwrap.md)
- [`kSecAttrCanUnwrap`](ksecattrcanunwrap.md)

These values default to `true` if no value is specified.

## Parameters

- `parameters`: A parameter dictionary that describes the key. See the discussion for details.
- `keyData`: A   object that contains the raw key data.
- `error`: A pointer to a   variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreatefromdata(_:_:_:))*