# SecDecryptTransformGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a decryption transform belongs.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecDecryptTransformGetTypeID() -> CFTypeID
```

```c
CFTypeID SecDecryptTransformGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecTransform`](./sectransform.md) object meant for decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secdecrypttransformgettypeid())*