# SecDecryptTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a decryption transform object.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecDecryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform
```

```c
SecTransformRefSecDecryptTransformCreate(SecKeyRef keyRef, CFErrorRef*error);
```

#### Return Value

A pointer to a new transform or `nil` on error. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which decrypts data.

## Parameters

- `keyRef`: The key for the operation
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md). This pointer will be set if an error occurred. This value may be `NULL` if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secdecrypttransformcreate(_:_:))*