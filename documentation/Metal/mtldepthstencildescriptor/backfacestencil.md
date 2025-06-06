# backFaceStencil

**Framework**: Metal  
**Kind**: property

The stencil descriptor for back-facing primitives.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var backFaceStencil: MTLStencilDescriptor! { get set }
```

#### Discussion

The default value is `nil`, which indicates the stencil test is disabled for the back-facing primitives. For more information, see [`MTLStencilDescriptor`](mtlstencildescriptor.md).

## See Also

- [var frontFaceStencil: MTLStencilDescriptor!](mtldepthstencildescriptor/frontfacestencil.md)
  The stencil descriptor for front-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/backfacestencil)*