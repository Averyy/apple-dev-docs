# ExecutorJob.LocalAllocator

**Framework**: Swift  
**Kind**: struct

A job-local stack-disciplined allocator.

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
struct LocalAllocator
```

#### Overview

This can be used to allocate additional data required by an executor implementation; memory allocated in this manner will be released automatically when the job is disposed of by the runtime.

N.B. Because this allocator is stack disciplined, explicitly deallocating memory out-of-order will cause your program to abort.

## Topics

### Instance Methods
- [func allocate<T>(as: T.Type) -> UnsafeMutablePointer<T>](executorjob/localallocator/allocate(as:).md)
  Allocate uninitialized memory for a single instance of type `T`.
- [func allocate(capacity: Int) -> UnsafeMutableRawBufferPointer](executorjob/localallocator/allocate(capacity:).md)
  Allocate a specified number of bytes of uninitialized memory.
- [func allocate<T>(capacity: Int, as: T.Type) -> UnsafeMutableBufferPointer<T>](executorjob/localallocator/allocate(capacity:as:).md)
  Allocate uninitialized memory for the specified number of instances of type `T`.
- [func deallocate<T>(UnsafeMutableBufferPointer<T>)](executorjob/localallocator/deallocate(_:)-6guut.md)
  Deallocate previously allocated memory.  Note that the task allocator is stack disciplined, so if you deallocate a block of memory, all memory allocated after that block is also deallocated.
- [func deallocate<T>(UnsafeMutablePointer<T>)](executorjob/localallocator/deallocate(_:)-91xo3.md)
  Deallocate previously allocated memory.  Note that the task allocator is stack disciplined, so if you deallocate a block of memory, all memory allocated after that block is also deallocated.
- [func deallocate(UnsafeMutableRawBufferPointer)](executorjob/localallocator/deallocate(_:)-9g62s.md)
  Deallocate previously allocated memory.  Note that the task allocator is stack disciplined, so if you deallocate a block of memory, all memory allocated after that block is also deallocated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/localallocator)*