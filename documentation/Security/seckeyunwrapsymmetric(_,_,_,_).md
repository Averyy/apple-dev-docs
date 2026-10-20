# SecKeyUnwrapSymmetric(_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Unwraps a wrapped symmetric key.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: No longer supported

## Declaration

```swift
func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

```c
SecKeyRefSecKeyUnwrapSymmetric(CFDataRef*keyToUnwrap, SecKeyRef unwrappingKey, CFDictionaryRef parameters, CFErrorRef*error);
```

#### Return Value

The unwrapped key, or `NULL` on failure. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free the key’s memory when you are done with it.

## Parameters

- `keyToUnwrap`: The wrapped key to unwrap.
- `unwrappingKey`: The key that must be used to unwrap `keyToUnwrap`.
- `parameters`: A parameter list for the unwrapping process. This is usually either an empty dictionary or a dictionary containing a value for [`kSecAttrSalt`](./ksecattrsalt.md).
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyunwrapsymmetric(_:_:_:_:))*