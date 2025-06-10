# maxTransferRate

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM).

**Availability**:
- macOS 10.15+

## Declaration

```swift
var maxTransferRate: UInt64 { get }
```

#### Discussion

Metal calculates this value from the raw data-clock rate, and the GPU may not be able to reach this speed in real-world conditions.

> ❗ **Important**:  The maximum transfer rate for built-in GPUs is `0`.

## See Also

- [var currentAllocatedSize: Int](mtldevice/currentallocatedsize.md)
  The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [var recommendedMaxWorkingSetSize: UInt64](mtldevice/recommendedmaxworkingsetsize.md)
  An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [var hasUnifiedMemory: Bool](mtldevice/hasunifiedmemory.md)
  A Boolean value that indicates whether the GPU shares all of its memory with the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maxtransferrate)*