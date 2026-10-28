# CVBufferRetain

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retains a Core Video buffer.

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
extern CVBufferRefCVBufferRetain(CVBufferRef buffer);
```

## Return Value

For convenience, the same Core Video buffer you wanted to retain.

## Discussion

Like [`CFRetain`](../CoreFoundation/cfretain.md), this function increments the retain count of a Core Video buffer. However, unlike [`CFRetain`](../CoreFoundation/cfretain.md), this function is `NULL` safe.

## Parameters

- `buffer`: The Core Video buffer that you want to retain.

## See Also

### Retaining and releasing buffers
- [CVBufferRelease](./cvbufferrelease.md)
  Releases a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbufferretain)*