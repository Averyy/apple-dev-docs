# MTLIOPriority.high

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Sets a new input/output command queue’s priority to a high priority.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case high
```

```c
MTLIOPriorityHigh
```

## Discussion

Create a command queue with a high priority to load important assets or those your app needs quickly. For example, a game that plays sound effects that match its animations can load its audio assets with low latency with a high priority queue.

## See Also

### I/O command queue priorities
- [MTLIOPriority.normal](./normal.md)
  Designates the normal priority for a new input/output command queue.
- [MTLIOPriority.low](./low.md)
  Designates the low priority for a new input/output command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliopriority/high)*