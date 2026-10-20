# SecEncodeTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates an encode transform object.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecEncodeTransformCreate(_ encodeType: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

```c
SecTransformRefSecEncodeTransformCreate(CFTypeRef encodeType, CFErrorRef*error);
```

#### Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which computes an encode.

## Parameters

- `encodeType`: The type of digest to compute. You may pass `NULL` for this parameter, in which case an appropriate algorithm will be chosen for you. See `Encoding Types` for a list of valid values.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md). This pointer will be set if an error occurred. This value may be `nil` if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secencodetransformcreate(_:_:))*