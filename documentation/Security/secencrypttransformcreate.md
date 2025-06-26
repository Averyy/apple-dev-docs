# SecEncryptTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func

Creates an encryption transform object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecEncryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform
```

#### Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which encrypts data.

## Parameters

- `keyRef`: The key for the encryption operation
- `error`: A pointer to a  . This pointer will be set if an error occurred. This value may be   if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secencrypttransformcreate(_:_:))*