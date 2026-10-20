# init(forOfflineGPUAt:colorSpace:options:sharedContext:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 10.10+ - Deprecated in 10.14

> **Deprecated**: Core Image OpenGL API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
init?(forOfflineGPUAt index: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]? = nil, sharedContext: CGLContextObj?)
```

```objc
+ (CIContext *) contextForOfflineGPUAtIndex:(unsigned int) index colorSpace:(CGColorSpaceRef) colorSpace options:(NSDictionary<NSString *,id> *) options sharedContext:(CGLContextObj) sharedContext;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(forofflinegpuat:colorspace:options:sharedcontext:))*