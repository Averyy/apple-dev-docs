# SecTransformCreateReadTransformWithReadStream(_:)

**Framework**: Security  
**Kind**: func

Creates a read transform from a read stream reference.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformCreateReadTransformWithReadStream(_ inputStream: CFReadStream) -> SecTransform
```

#### Return Value

A pointer to a new transform. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free this object’s memory when you are done with it.

## Parameters

- `inputStream`: The stream that is to be opened and read from when the chain executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcreatereadtransformwithreadstream(_:))*