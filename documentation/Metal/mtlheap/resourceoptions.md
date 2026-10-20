# resourceOptions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The options for resources created by the heap.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var resourceOptions: MTLResourceOptions { get }
```

```objc
@property (readonly) MTLResourceOptions resourceOptions;
```

#### Discussion

The value of this property aggregates the values of [`storageMode`](./storagemode.md), [`cpuCacheMode`](./cpucachemode.md), and [`hazardTrackingMode`](./hazardtrackingmode.md).

## See Also

### Checking a heap’s permanent configuration
- [var device: any MTLDevice](./device.md)
  The device object that created the heap.
- [var type: MTLHeapType](./type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The heap’s storage mode.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The heap’s CPU cache mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The heap’s hazard tracking mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/resourceoptions)*