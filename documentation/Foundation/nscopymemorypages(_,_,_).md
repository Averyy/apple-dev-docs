# NSCopyMemoryPages(_:_:_:)

**Framework**: Foundation  
**Kind**: func

Copies a block of memory.

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
func NSCopyMemoryPages(_ source: UnsafeRawPointer, _ dest: UnsafeMutableRawPointer, _ bytes: Int)
```

#### Discussion

Copies (or copies on write) `byteCount` bytes from `source` to `destination`.

## See Also

- [func NSAllocateMemoryPages(Int) -> UnsafeMutableRawPointer](nsallocatememorypages(_:).md)
  Allocates a new block of memory.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscopymemorypages(_:_:_:))*