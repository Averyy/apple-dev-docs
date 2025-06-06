# version

**Framework**: Core Media  
**Kind**: property

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
var version: UInt32
```

## See Also

- [var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?](cmblockbuffercustomblocksource/allocateblock.md)
  The function to allocate memory.
- [var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Void)?](cmblockbuffercustomblocksource/freeblock.md)
  A function to call once when the `CMBlockBuffer` is disposed.
- [var refCon: UnsafeMutableRawPointer?](cmblockbuffercustomblocksource/refcon.md)
  Contextual information passed to both the allocate and free function calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/version)*