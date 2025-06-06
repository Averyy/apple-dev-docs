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

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which computes a decode.

## Parameters

- `DecodeType`: The type of digest to decode. You may pass   for this parameter, in which case an appropriate algorithm will be chosen for you. See   for a list of valid values.
- `error`: A pointer to a  doc://com.apple.documentation/documentation/corefoundation/cferror-ru8 . This pointer will be set if an error occurred. This value may be   if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secdecodetransformcreate(_:_:))*