# CGBitmapContextCreateAdaptive

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
extern CGContextRefCGBitmapContextCreateAdaptive(size_t width, size_t height, CFDictionaryRef auxiliaryInfo, bool (^onResolve)(const CGContentInfo *, CGBitmapParameters *), CGRenderingBufferProviderRef (^onAllocate)(const CGContentInfo *, const CGBitmapParameters *), void (^onFree)(CGRenderingBufferProviderRef , const CGContentInfo *, const CGBitmapParameters *), void (^onError)(CFErrorRef , const CGContentInfo *, const CGBitmapParameters *));
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgbitmapcontextcreateadaptive)*