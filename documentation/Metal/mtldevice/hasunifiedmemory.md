# hasUnifiedMemory

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the GPU shares all of its memory with the CPU.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var hasUnifiedMemory: Bool { get }
```

```objc
@property (readonly) BOOL hasUnifiedMemory;
```

## Discussion

A GPU with unified memory ([`true`](../../Swift/true.md)) is typically an integrated GPU. A GPU with dedicated memory ([`false`](../../Swift/false.md)) may take additional time to synchronize managed resources or copy data into private GPU resources.

## See Also

### Checking a GPU device’s memory
- [var currentAllocatedSize: Int](./currentallocatedsize.md)
  The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [var recommendedMaxWorkingSetSize: UInt64](./recommendedmaxworkingsetsize.md)
  An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [var maxTransferRate: UInt64](./maxtransferrate.md)
  The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory)*