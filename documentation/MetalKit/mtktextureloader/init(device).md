# init(device:)

**Framework**: MetalKit  
**Kind**: init  
**Role**: Initializer

Initializes a new texture loader object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device;
```

#### Return Value

An initialized texture loader object.

## Parameters

- `device`: The Metal device to create Metal textures with.

## See Also

### Creating a Texture Loader
- [var device: any MTLDevice](./device.md)
  The device object that the texture loader uses to create textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/init(device:))*