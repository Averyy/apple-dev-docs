# refCon

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

Contextual information passed to both the allocate and free function calls.

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
var refCon: UnsafeMutableRawPointer?
```

```c
void * refCon;
```

## See Also

### Properties
- [var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?](./allocateblock.md)
  The function to allocate memory.
- [var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Void)?](./freeblock.md)
  A function to call once when the `CMBlockBuffer` is disposed.
- [var version: UInt32](./version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/refcon)*