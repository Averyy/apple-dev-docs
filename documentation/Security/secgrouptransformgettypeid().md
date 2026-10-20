# SecGroupTransformGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the Core Foundation type ID for a transform group container.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecGroupTransformGetTypeID() -> CFTypeID
```

```c
extern CFTypeID SecGroupTransformGetTypeID();
```

#### Return Value

A value that identifies the opaque type of a [`SecGroupTransform`](./secgrouptransform.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secgrouptransformgettypeid())*