# SecKeyWrapSymmetric(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Wraps a symmetric key with another key.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyWrapSymmetric(_ keyToWrap: SecKey, _ wrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

#### Return Value

The wrapped key, or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free the data’s memory when you are done with it.

## Parameters

- `keyToWrap`: The key to wrap.
- `wrappingKey`: The key to use when wrapping  .
- `parameters`: A parameter list for the unwrapping process. This is usually either an empty dictionary or a dictionary containing a value for  .
- `error`: A pointer to a   variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeywrapsymmetric(_:_:_:_:))*