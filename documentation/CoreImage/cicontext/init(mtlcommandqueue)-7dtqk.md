# init(mtlCommandQueue:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(mtlCommandQueue commandQueue: any MTLCommandQueue)
```

```objc
+ (CIContext *) contextWithMTLCommandQueue:(id<MTLCommandQueue>) commandQueue;
```

## See Also

### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice)](./init%28mtldevice%29-swey.md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlDevice: any MTLDevice, options: [CIContextOption : Any]?)](./init%28mtldevice,options%29-26usb.md)
  Creates a Core Image context using the specified Metal device and options.
- [init(mtlCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](./init%28mtlcommandqueue,options%29-6i3me.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(mtlcommandqueue:)-7dtqk)*