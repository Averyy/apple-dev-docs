# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The device object that created the heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (readonly) id<MTLDevice> device;
```

#### Discussion

A heap is always associated with the [`MTLDevice`](../mtldevice.md) that created it and can be used only with that device.

## See Also

### Checking a heap’s permanent configuration
- [var type: MTLHeapType](./type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The heap’s storage mode.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The heap’s CPU cache mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The heap’s hazard tracking mode.
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The options for resources created by the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/device)*