# NSAllocateMemoryPages(_:)

**Framework**: Foundation  
**Kind**: func

Allocates a new block of memory.

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
func NSAllocateMemoryPages(_ bytes: Int) -> UnsafeMutableRawPointer
```

#### Discussion

Allocates the integral number of pages whose total size is closest to, but not less than, `byteCount`. The allocated pages are guaranteed to be filled with zeros. If the allocation fails, raises `NSInvalidArgumentException`.

## See Also

- [func NSCopyMemoryPages(UnsafeRawPointer, UnsafeMutableRawPointer, Int)](nscopymemorypages(_:_:_:).md)
  Copies a block of memory.
- [func NSDeallocateMemoryPages(UnsafeMutableRawPointer, Int)](nsdeallocatememorypages(_:_:).md)
  Deallocates the specified block of memory.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsallocatememorypages(_:))*