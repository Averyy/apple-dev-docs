# SecTransformCreateReadTransformWithReadStream(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a read transform from a read stream reference.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformCreateReadTransformWithReadStream(_ inputStream: CFReadStream) -> SecTransform
```

```c
SecTransformRefSecTransformCreateReadTransformWithReadStream(CFReadStreamRef inputStream);
```

#### Return Value

A pointer to a new transform. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Parameters

- `inputStream`: The stream that is to be opened and read from when the chain executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcreatereadtransformwithreadstream(_:))*