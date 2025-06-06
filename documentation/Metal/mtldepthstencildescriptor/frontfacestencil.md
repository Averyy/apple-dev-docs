# frontFaceStencil

**Framework**: Metal  
**Kind**: property

The stencil descriptor for front-facing primitives.

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
var frontFaceStencil: MTLStencilDescriptor! { get set }
```

#### Discussion

The default value is `nil`, which indicates the stencil test is disabled for the front-facing primitives. For more information, see [`MTLStencilDescriptor`](mtlstencildescriptor.md).

## See Also

- [var backFaceStencil: MTLStencilDescriptor!](mtldepthstencildescriptor/backfacestencil.md)
  The stencil descriptor for back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/frontfacestencil)*