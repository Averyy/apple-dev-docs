# MPSSVGFDefaultTextureAllocator

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSSVGFDefaultTextureAllocator
```

```objc
@interface MPSSVGFDefaultTextureAllocator : NSObject
```

## Topics

### Initializers
- [init(device: any MTLDevice)](./mpssvgfdefaulttextureallocator/init%28device%29.md)
### Instance Properties
- [var allocatedTextureCount: Int](./mpssvgfdefaulttextureallocator/allocatedtexturecount.md)
- [var device: any MTLDevice](./mpssvgfdefaulttextureallocator/device.md)
### Instance Methods
- [func reset()](./mpssvgfdefaulttextureallocator/reset%28%29.md)
- [func `return`(any MTLTexture)](./mpssvgfdefaulttextureallocator/return%28_%29.md)
- [func texture(with: MTLPixelFormat, width: Int, height: Int) -> (any MTLTexture)?](./mpssvgfdefaulttextureallocator/texture%28with,width,height%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MPSSVGFTextureAllocator](./mpssvgftextureallocator.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdefaulttextureallocator)*