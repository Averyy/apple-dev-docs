# init(mtlDevice:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a Core Image context using the specified Metal device and options.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(mtlDevice device: any MTLDevice, options: [CIContextOption : Any]? = nil)
```

```objc
+ (CIContext *) contextWithMTLDevice:(id<MTLDevice>) device options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

A Core Image context.

#### Discussion

Use this method to choose a specific Metal device for rendering when a system contains multiple Metal devices. To create a Metal-based context using the system’s default Metal device, use the [`contextWithOptions:`](./contextwithoptions_.md) method.

## Parameters

- `device`: The Metal device object to use for rendering.
- `options`: A dictionary that contains options for creating a [`CIContext`](../cicontext.md) object. You can pass any of the keys defined in [`CIContextOption`](../cicontextoption.md) along with the appropriate value.

## See Also

### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice)](./init%28mtldevice%29-swey.md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlCommandQueue: any MTLCommandQueue)](./init%28mtlcommandqueue%29-7dtqk.md)
- [init(mtlCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](./init%28mtlcommandqueue,options%29-6i3me.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(mtldevice:options:)-26usb)*