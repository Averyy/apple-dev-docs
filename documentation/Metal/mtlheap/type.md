# type

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The heap’s type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var type: MTLHeapType { get }
```

```objc
@property (readonly) MTLHeapType type;
```

## See Also

### Checking a heap’s permanent configuration
- [var device: any MTLDevice](./device.md)
  The device object that created the heap.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The heap’s storage mode.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The heap’s CPU cache mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The heap’s hazard tracking mode.
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The options for resources created by the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/type)*