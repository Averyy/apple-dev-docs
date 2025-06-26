# SecKeyUnwrapSymmetric(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Unwraps a wrapped symmetric key.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

#### Return Value

The unwrapped key, or `NULL` on failure. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the key’s memory when you are done with it.

## Parameters

- `keyToUnwrap`: The wrapped key to unwrap.
- `unwrappingKey`: The key that must be used to unwrap  .
- `parameters`: A parameter list for the unwrapping process. This is usually either an empty dictionary or a dictionary containing a value for  .
- `error`: A pointer to a   variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyunwrapsymmetric(_:_:_:_:))*