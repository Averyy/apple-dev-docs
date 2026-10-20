# NSAllocateMemoryPages(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern void *NSAllocateMemoryPages(NSUInteger bytes);
```

#### Discussion

Allocates the integral number of pages whose total size is closest to, but not less than, `byteCount`. The allocated pages are guaranteed to be filled with zeros. If the allocation fails, raises `NSInvalidArgumentException`.

## See Also

### Memory Management
- [func NSCopyMemoryPages(UnsafeRawPointer, UnsafeMutableRawPointer, Int)](./nscopymemorypages%28_,_,_%29.md)
  Copies a block of memory.
- [func NSDeallocateMemoryPages(UnsafeMutableRawPointer, Int)](./nsdeallocatememorypages%28_,_%29.md)
  Deallocates the specified block of memory.
- [func NSLogPageSize() -> Int](./nslogpagesize%28%29.md)
  Returns the binary log of the page size.
- [func NSPageSize() -> Int](./nspagesize%28%29.md)
  Returns the number of bytes in a page.
- [func NSRealMemoryAvailable() -> Int](./nsrealmemoryavailable%28%29.md)
  Returns information about the user’s system.
- [func NSRoundDownToMultipleOfPageSize(Int) -> Int](./nsrounddowntomultipleofpagesize%28_%29.md)
  Returns the specified number of bytes rounded down to a multiple of the page size.
- [func NSRoundUpToMultipleOfPageSize(Int) -> Int](./nsrounduptomultipleofpagesize%28_%29.md)
  Returns the specified number of bytes rounded up to a multiple of the page size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsallocatememorypages(_:))*