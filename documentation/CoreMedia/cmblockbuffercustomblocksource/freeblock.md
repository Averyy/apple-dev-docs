# FreeBlock

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

A function to call once when the `CMBlockBuffer` is disposed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Void)?
```

```c
void (*)(void *, void *, unsigned long) FreeBlock;
```

#### Discussion

Pass `NULL` if you don’t want a function to be called after disposal. The function will not be called if no memory block is ever allocated or supplied.

## See Also

### Properties
- [var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?](./allocateblock.md)
  The function to allocate memory.
- [var refCon: UnsafeMutableRawPointer?](./refcon.md)
  Contextual information passed to both the allocate and free function calls.
- [var version: UInt32](./version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/freeblock)*