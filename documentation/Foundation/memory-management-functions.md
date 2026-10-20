# Memory Management Functions

**Framework**: Foundation  
**Role**: API Collection

Perform low-level memory management tasks.

## Topics

### Core Foundation ARC Integration
- [func CFBridgingRetain(Any?) -> CFTypeRef?](./cfbridgingretain%28_%29.md)
  Casts an Objective-C pointer to a Core Foundation pointer and also transfers ownership to the caller.
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
- [func NSRealMemoryAvailable() -> Int](./nsrealmemoryavailable%28%29.md)
  Returns information about the user’s system.
- [func NSRoundDownToMultipleOfPageSize(Int) -> Int](./nsrounddowntomultipleofpagesize%28_%29.md)
  Returns the specified number of bytes rounded down to a multiple of the page size.
- [func NSRoundUpToMultipleOfPageSize(Int) -> Int](./nsrounduptomultipleofpagesize%28_%29.md)
  Returns the specified number of bytes rounded up to a multiple of the page size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/memory-management-functions)*