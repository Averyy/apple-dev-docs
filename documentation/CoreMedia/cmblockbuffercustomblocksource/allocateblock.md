# AllocateBlock

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The function to allocate memory.

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
var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?
```

```c
void *(*)(void *, unsigned long) AllocateBlock;
```

## See Also

### Properties
- [var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Void)?](./freeblock.md)
  A function to call once when the `CMBlockBuffer` is disposed.
- [var refCon: UnsafeMutableRawPointer?](./refcon.md)
  Contextual information passed to both the allocate and free function calls.
- [var version: UInt32](./version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/allocateblock)*