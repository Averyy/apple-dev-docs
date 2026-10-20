# cpuCacheMode

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The heap’s CPU cache mode.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cpuCacheMode: MTLCPUCacheMode { get }
```

```objc
@property (readonly) MTLCPUCacheMode cpuCacheMode;
```

#### Discussion

Any resources you allocate on the heap have this CPU cache mode.

## See Also

### Checking a heap’s permanent configuration
- [var device: any MTLDevice](./device.md)
  The device object that created the heap.
- [var type: MTLHeapType](./type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The heap’s storage mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The heap’s hazard tracking mode.
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The options for resources created by the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/cpucachemode)*