# NSRealMemoryAvailable()

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns information about the user’s system.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 2.0+ - Deprecated in 6.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use NSProcessInfo instead

## Declaration

```swift
func NSRealMemoryAvailable() -> Int
```

```c
extern NSUInteger NSRealMemoryAvailable();
```

#### Return Value

The number of bytes available in RAM.

## See Also

### Memory Management
- [func NSAllocateMemoryPages(Int) -> UnsafeMutableRawPointer](./nsallocatememorypages%28_%29.md)
  Allocates a new block of memory.
- [func NSCopyMemoryPages(UnsafeRawPointer, UnsafeMutableRawPointer, Int)](./nscopymemorypages%28_,_,_%29.md)
  Copies a block of memory.
- [func NSDeallocateMemoryPages(UnsafeMutableRawPointer, Int)](./nsdeallocatememorypages%28_,_%29.md)
  Deallocates the specified block of memory.
- [func NSLogPageSize() -> Int](./nslogpagesize%28%29.md)
  Returns the binary log of the page size.
- [func NSPageSize() -> Int](./nspagesize%28%29.md)
  Returns the number of bytes in a page.
- [func NSRoundDownToMultipleOfPageSize(Int) -> Int](./nsrounddowntomultipleofpagesize%28_%29.md)
  Returns the specified number of bytes rounded down to a multiple of the page size.
- [func NSRoundUpToMultipleOfPageSize(Int) -> Int](./nsrounduptomultipleofpagesize%28_%29.md)
  Returns the specified number of bytes rounded up to a multiple of the page size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrealmemoryavailable())*