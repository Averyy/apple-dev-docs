# device

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The device object that the texture loader uses to create textures.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (nonatomic, readonly, nonnull) id<MTLDevice> device;
```

## See Also

### Creating a Texture Loader
- [init(device: any MTLDevice)](./init%28device%29.md)
  Initializes a new texture loader object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/device)*