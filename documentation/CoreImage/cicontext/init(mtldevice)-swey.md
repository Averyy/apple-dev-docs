# init(mtlDevice:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a Core Image context using the specified Metal device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(mtlDevice device: any MTLDevice)
```

```objc
+ (CIContext *) contextWithMTLDevice:(id<MTLDevice>) device;
```

#### Return Value

A Core Image context.

#### Discussion

Use this method to choose a specific Metal device for rendering when a system contains multiple Metal devices. To create a Metal-based context using the system’s default Metal device, use the [`contextWithOptions:`](./contextwithoptions_.md) method.

## Parameters

- `device`: The Metal device object to use for rendering.

## See Also

### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice, options: [CIContextOption : Any]?)](./init%28mtldevice,options%29-26usb.md)
  Creates a Core Image context using the specified Metal device and options.
- [init(mtlCommandQueue: any MTLCommandQueue)](./init%28mtlcommandqueue%29-7dtqk.md)
- [init(mtlCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](./init%28mtlcommandqueue,options%29-6i3me.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(mtldevice:)-swey)*