# CGRenderingBufferProviderCreate

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
extern CGRenderingBufferProviderRefCGRenderingBufferProviderCreate(void *info, size_t size, void * (^lockPointer)(void *info), void (^unlockPointer)(void *info, void *pointer), void (^releaseInfo)(void *info));
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrenderingbufferprovidercreate)*