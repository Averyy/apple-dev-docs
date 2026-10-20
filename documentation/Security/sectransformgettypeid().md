# SecTransformGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a security transform object belongs.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformGetTypeID() -> CFTypeID
```

```c
extern CFTypeID SecTransformGetTypeID();
```

#### Return Value

A value that identifies the opaque type of a [`SecTransform`](./sectransform.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformgettypeid())*