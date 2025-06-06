# AllocateBlock

**Framework**: Core Media  
**Kind**: property

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

## See Also

- [var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Void)?](cmblockbuffercustomblocksource/freeblock.md)
  A function to call once when the `CMBlockBuffer` is disposed.
- [var refCon: UnsafeMutableRawPointer?](cmblockbuffercustomblocksource/refcon.md)
  Contextual information passed to both the allocate and free function calls.
- [var version: UInt32](cmblockbuffercustomblocksource/version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/allocateblock)*