# acquiring

**Framework**: Synchronization  
**Kind**: property

An acquiring load synchronizes with a releasing operation whose value its reads. It ensures that the releasing and acquiring threads agree that all subsequent variable accesses on the acquiring thread happen after the atomic operation itself.

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
static var acquiring: AtomicLoadOrdering { get }
```

#### Discussion

This value corresponds to `std::memory_order_acquire` in C++.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicloadordering/acquiring)*