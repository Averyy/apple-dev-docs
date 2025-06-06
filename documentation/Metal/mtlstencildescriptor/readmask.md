# readMask

**Framework**: Metal  
**Kind**: property

A bitmask that determines from which bits that stencil comparison tests can read.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var readMask: UInt32 { get set }
```

#### Discussion

The [`readMask`](mtlstencildescriptor/readmask.md) bits are used for logical AND operations to both the stored stencil value and the reference value.

The least significant bits of the read mask are used. The default value is all ones. A logical AND operation with the default [`readMask`](mtlstencildescriptor/readmask.md) does not change the value.

## See Also

- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [var writeMask: UInt32](mtlstencildescriptor/writemask.md)
  A bitmask that determines to which bits that stencil operations can write.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor/readmask)*