# init(ink:path:transform:mask:randomSeed:id:renderGroupID:renderState:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform = .identity, mask: NSBezierPath? = nil, randomSeed: UInt32 = UInt32.random(in: 0...UInt32.max), id: UUID = UUID(), renderGroupID: UUID? = nil, renderState: PKStroke.RenderState? = nil)
```

## See Also

### Creating a stroke object
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](./init%28ink,path,transform,mask%29-1imp6.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?)](./init%28ink,path,transform,mask%29-w7ti.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](./init%28ink,path,transform,mask,randomseed%29-10m5j.md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32)](./init%28ink,path,transform,mask,randomseed%29-epus.md)
  Creates a macOS stroke with the line properties, path, transform, mask, and random seed that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32, id: UUID, renderGroupID: UUID?, renderState: PKStroke.RenderState?)](./init%28ink,path,transform,mask,randomseed,id,rendergroupid,renderstate%29-idqu.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:id:rendergroupid:renderstate:)-1qvj7)*