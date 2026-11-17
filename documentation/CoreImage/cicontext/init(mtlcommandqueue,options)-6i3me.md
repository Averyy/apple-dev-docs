# init(mtlCommandQueue:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a Core Image context that commits commands to the specified Metal command queue.

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

## Return Value

A Core Image context.

## Parameters

- `commandQueue`: The Metal command queue to use for operations.
- `options`: A dictionary that contains options for creating a [`CIContext`](../cicontext.md) object. You can pass any of the keys defined in [`CIContextOption`](../cicontextoption.md) along with the appropriate value.

## See Also

### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice)](./init%28mtldevice%29-swey.md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlDevice: any MTLDevice, options: [CIContextOption : Any]?)](./init%28mtldevice,options%29-26usb.md)
  Creates a Core Image context using the specified Metal device and options.
- [init(mtlCommandQueue: any MTLCommandQueue)](./init%28mtlcommandqueue%29-7dtqk.md)
  Creates a Core Image context that commits commands to the specified Metal command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(mtlcommandqueue:options:)-6i3me)*