# SecDigestTransformCreate(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a digest transform object.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecDigestTransformCreate(_ digestType: CFTypeRef?, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform
```

```c
SecTransformRefSecDigestTransformCreate(CFTypeRef digestType, CFIndex digestLength, CFErrorRef*error);
```

## Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

This function creates a transform which computes a cryptographic digest.

## Parameters

- `digestType`: The type of digest to compute. You may pass `NULL` for this parameter, in which case an appropriate algorithm will be chosen for you. Otherwise, use one of the values listed in `Digest Constants`.
- `digestLength`: The desired digest length. Note that certain algorithms may only support certain sizes. You may pass `0` for this parameter, in which case an appropriate length will be chosen for you.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md). This pointer will be set if an error occurred. This value may be `nil` if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secdigesttransformcreate(_:_:_:))*