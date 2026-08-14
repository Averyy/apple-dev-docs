# SecDecodeTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func

Creates a decode transform object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecDecodeTransformCreate(_ DecodeType: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

#### Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/cfrelease) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which computes a decode.

## Parameters

- `DecodeType`: The type of digest to decode. You may pass `NULL` for this parameter, in which case an appropriate algorithm will be chosen for you. See `Encoding Types` for a list of valid values.
- `error`: A pointer to a [`CFError`](https://developer.apple.com/documentation/corefoundation/cferror). This pointer will be set if an error occurred. This value may be `NULL` if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secdecodetransformcreate(_:_:))*