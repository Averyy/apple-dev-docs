# acquiringAndReleasing

**Framework**: Synchronization  
**Kind**: property

An acquiring-and-releasing operation is a combination of `.acquiring` and `.releasing` operation on the same variable.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static var acquiringAndReleasing: AtomicUpdateOrdering { get }
```

#### Discussion

This value corresponds to `std::memory_order_acq_rel` in C++.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicupdateordering/acquiringandreleasing)*