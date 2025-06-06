# currentAllocatedSize

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The total amount of memory, in bytes, the GPU device is using for all of its resources.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var currentAllocatedSize: Int { get }
```

## See Also

- [var recommendedMaxWorkingSetSize: UInt64](mtldevice/recommendedmaxworkingsetsize.md)
  An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [var hasUnifiedMemory: Bool](mtldevice/hasunifiedmemory.md)
  A Boolean value that indicates whether the GPU shares all of its memory with the CPU.
- [var maxTransferRate: UInt64](mtldevice/maxtransferrate.md)
  The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/currentallocatedsize)*