# recommendedMaxWorkingSetSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var recommendedMaxWorkingSetSize: UInt64 { get }
```

```objc
@property (readonly) uint64_t recommendedMaxWorkingSetSize;
```

#### Discussion

You can help the GPU maintain its performance by keeping the total memory footprint of its resources and heaps less than this threshold value.

## See Also

### Checking a GPU device’s memory
- [var currentAllocatedSize: Int](./currentallocatedsize.md)
  The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [var hasUnifiedMemory: Bool](./hasunifiedmemory.md)
  A Boolean value that indicates whether the GPU shares all of its memory with the CPU.
- [var maxTransferRate: UInt64](./maxtransferrate.md)
  The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/recommendedmaxworkingsetsize)*