# frontFaceStencil

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The stencil descriptor for front-facing primitives.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var frontFaceStencil: MTLStencilDescriptor! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) MTLStencilDescriptor * frontFaceStencil;
```

## Discussion

The default value is `nil`, which indicates the stencil test is disabled for the front-facing primitives. For more information, see [`MTLStencilDescriptor`](../mtlstencildescriptor.md).

## See Also

### Specifying stencil descriptors for primitives
- [var backFaceStencil: MTLStencilDescriptor!](./backfacestencil.md)
  The stencil descriptor for back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/frontfacestencil)*