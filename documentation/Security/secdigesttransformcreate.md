# SecDigestTransformCreate(_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a digest transform object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecDigestTransformCreate(_ digestType: CFTypeRef?, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform
```

#### Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which computes a cryptographic digest.

## Parameters

- `digestType`: The type of digest to compute. You may pass   for this parameter, in which case an appropriate algorithm will be chosen for you. Otherwise, use one of the values listed in  .
- `digestLength`: The desired digest length. Note that certain algorithms may only support certain sizes. You may pass   for this parameter, in which case an appropriate length will be chosen for you.
- `error`: A pointer to a  . This pointer will be set if an error occurred. This value may be   if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secdigesttransformcreate(_:_:_:))*