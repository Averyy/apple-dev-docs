# writeMask

**Framework**: Metal  
**Kind**: property

A bitmask that determines to which bits that stencil operations can write.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var writeMask: UInt32 { get set }
```

#### Discussion

[`writeMask`](mtlstencildescriptor/writemask.md) are used for logical AND operations to values that are going to be written into a stencil attachment as the result of a stencil operation.

The least significant bits of the write mask are used. The default value is all ones. A logical AND operation with the default [`writeMask`](mtlstencildescriptor/writemask.md) does not change the value.

## See Also

- [var readMask: UInt32](mtlstencildescriptor/readmask.md)
  A bitmask that determines from which bits that stencil comparison tests can read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor/writemask)*