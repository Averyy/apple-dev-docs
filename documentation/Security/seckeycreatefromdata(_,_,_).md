# SecKeyCreateFromData(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Constructs a SecKeyRef object for a symmetric key.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: No longer supported

## Declaration

```swift
func SecKeyCreateFromData(_ parameters: CFDictionary, _ keyData: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

```c
SecKeyRefSecKeyCreateFromData(CFDictionaryRef parameters, CFDataRef keyData, CFErrorRef*error);
```

## Return Value

A symmetric key. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free the key’s memory when you are done with it.

## Discussion

The parameters dictionary must contain (at minimum) an entry for the [`kSecAttrKeyType`](./ksecattrkeytype.md) key with a value of [`kSecAttrKeyTypeAES`](./ksecattrkeytypeaes.md) or any other key type defined in Key Type Value.

The keys below may be optionally set in the parameters dictionary (with a `CFBooleanRef` value) to override the default key usage values:

- [`kSecAttrCanEncrypt`](./ksecattrcanencrypt.md)
- [`kSecAttrCanDecrypt`](./ksecattrcandecrypt.md)
- [`kSecAttrCanWrap`](./ksecattrcanwrap.md)
- [`kSecAttrCanUnwrap`](./ksecattrcanunwrap.md)

These values default to `true` if no value is specified.

## Parameters

- `parameters`: A parameter dictionary that describes the key. See the discussion for details.
- `keyData`: A `CFDataRef` object that contains the raw key data.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreatefromdata(_:_:_:))*