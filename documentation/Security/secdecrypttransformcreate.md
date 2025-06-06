# SecDecryptTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func

Creates a decryption transform object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecDecryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform
```

#### Return Value

A pointer to a new transform or `nil` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which decrypts data.

## Parameters

- `keyRef`: The key for the operation
- `error`: A pointer to a  doc://com.apple.documentation/documentation/corefoundation/cferror-ru8 . This pointer will be set if an error occurred. This value may be   if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secdecrypttransformcreate(_:_:))*