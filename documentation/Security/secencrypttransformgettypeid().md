# SecEncryptTransformGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which an encryption transform belongs.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecEncryptTransformGetTypeID() -> CFTypeID
```

```c
CFTypeID SecEncryptTransformGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecTransform`](./sectransform.md) object meant for encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secencrypttransformgettypeid())*