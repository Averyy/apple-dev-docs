# NSDeallocateMemoryPages(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern void NSDeallocateMemoryPages(void *ptr, NSUInteger bytes);
```

## Discussion

This function deallocates memory that was allocated with `NSAllocateMemoryPages`.

## See Also

### Memory Management
- [func NSAllocateMemoryPages(Int) -> UnsafeMutableRawPointer](./nsallocatememorypages%28_%29.md)
  Allocates a new block of memory.
- [func NSCopyMemoryPages(UnsafeRawPointer, UnsafeMutableRawPointer, Int)](./nscopymemorypages%28_,_,_%29.md)
  Copies a block of memory.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdeallocatememorypages(_:_:))*