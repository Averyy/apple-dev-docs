# init(mtlCommandQueue:options:)

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
init(mtlCommandQueue commandQueue: any MTLCommandQueue, options: [CIContextOption : Any]? = nil)
```

```objc
+ (CIContext *) contextWithMTLCommandQueue:(id<MTLCommandQueue>) commandQueue options:(NSDictionary<NSString *,id> *) options;
```

## See Also

### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice)](./init%28mtldevice%29-swey.md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlDevice: any MTLDevice, options: [CIContextOption : Any]?)](./init%28mtldevice,options%29-26usb.md)
  Creates a Core Image context using the specified Metal device and options.
- [init(mtlCommandQueue: any MTLCommandQueue)](./init%28mtlcommandqueue%29-7dtqk.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(mtlcommandqueue:options:)-6i3me)*