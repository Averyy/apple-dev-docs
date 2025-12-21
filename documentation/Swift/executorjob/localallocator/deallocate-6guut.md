# deallocate(_:)

**Framework**: Swift  
**Kind**: method

Deallocate previously allocated memory.  Note that the task allocator is stack disciplined, so if you deallocate a block of memory, all memory allocated after that block is also deallocated.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func deallocate<T>(_ buffer: UnsafeMutableBufferPointer<T>)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/localallocator/deallocate(_:)-6guut)*