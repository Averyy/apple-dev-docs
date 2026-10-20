# SecKeyWrapSymmetric(_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Wraps a symmetric key with another key.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: No longer supported

## Declaration

```swift
func SecKeyWrapSymmetric(_ keyToWrap: SecKey, _ wrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

```c
CFDataRefSecKeyWrapSymmetric(SecKeyRef keyToWrap, SecKeyRef wrappingKey, CFDictionaryRef parameters, CFErrorRef*error);
```

#### Return Value

The wrapped key, or `NULL` on error. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free the data’s memory when you are done with it.

## Parameters

- `keyToWrap`: The key to wrap.
- `wrappingKey`: The key to use when wrapping `keyToWrap`.
- `parameters`: A parameter list for the unwrapping process. This is usually either an empty dictionary or a dictionary containing a value for [`kSecAttrSalt`](./ksecattrsalt.md).
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeywrapsymmetric(_:_:_:_:))*