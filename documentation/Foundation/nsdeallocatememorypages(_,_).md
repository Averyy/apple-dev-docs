# NSDeallocateMemoryPages(_:_:)

**Framework**: Foundation  
**Kind**: func

Deallocates the specified block of memory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSDeallocateMemoryPages(_ ptr: UnsafeMutableRawPointer, _ bytes: Int)
```

#### Discussion

This function deallocates memory that was allocated with `NSAllocateMemoryPages`.

## See Also

- [func NSAllocateMemoryPages(Int) -> UnsafeMutableRawPointer](nsallocatememorypages(_:).md)
  Allocates a new block of memory.
- [func NSCopyMemoryPages(UnsafeRawPointer, UnsafeMutableRawPointer, Int)](nscopymemorypages(_:_:_:).md)
  Copies a block of memory.
- [func NSLogPageSize() -> Int](nslogpagesize().md)
  Returns the binary log of the page size.
- [func NSPageSize() -> Int](nspagesize().md)
  Returns the number of bytes in a page.
- [func NSRealMemoryAvailable() -> Int](nsrealmemoryavailable().md)
  Returns information about the user’s system.
- [func NSRoundDownToMultipleOfPageSize(Int) -> Int](nsrounddowntomultipleofpagesize(_:).md)
  Returns the specified number of bytes rounded down to a multiple of the page size.
- [func NSRoundUpToMultipleOfPageSize(Int) -> Int](nsrounduptomultipleofpagesize(_:).md)
  Returns the specified number of bytes rounded up to a multiple of the page size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdeallocatememorypages(_:_:))*