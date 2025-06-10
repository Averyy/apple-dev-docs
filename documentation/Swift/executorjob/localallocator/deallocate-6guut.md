# deallocate(_:)

**Framework**: Swift  
**Kind**: method

Deallocate previously allocated memory.  Note that the task allocator is stack disciplined, so if you deallocate a block of memory, all memory allocated after that block is also deallocated.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func deallocate<T>(_ buffer: UnsafeMutableBufferPointer<T>)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/localallocator/deallocate(_:)-6guut)*