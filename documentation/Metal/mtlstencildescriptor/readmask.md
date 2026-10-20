# readMask

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A bitmask that determines from which bits that stencil comparison tests can read.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var readMask: UInt32 { get set }
```

```objc
@property (nonatomic) uint32_t readMask;
```

#### Discussion

The [`readMask`](./readmask.md) bits are used for logical AND operations to both the stored stencil value and the reference value.

The least significant bits of the read mask are used. The default value is all ones. A logical AND operation with the default [`readMask`](./readmask.md) does not change the value.

## See Also

### Related Documentation
- [func setStencilReferenceValue(UInt32)](../mtlrendercommandencoder/setstencilreferencevalue%28_%29.md)
  Configures the same comparison value for front- and back-facing primitives.
### Configuring stencil bit mask properties
- [var writeMask: UInt32](./writemask.md)
  A bitmask that determines to which bits that stencil operations can write.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor/readmask)*