# CVBufferRelease

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Releases a Core Video buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CVBufferRelease(CVBufferRef buffer);
```

#### Discussion

Like [`CFRelease`](../CoreFoundation/cfrelease.md), this function decrements the retain count of a Core Video buffer. However, unlike [`CFRelease`](../CoreFoundation/cfrelease.md), this function is `NULL` safe. If the retain count becomes zero, the system deallocates the object.

## Parameters

- `buffer`: The Core Video buffer that you want to release.

## See Also

### Retaining and releasing buffers
- [CVBufferRetain](./cvbufferretain.md)
  Retains a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbufferrelease)*