# isWatertight

**Framework**: RealityKit  
**Kind**: property

Indicates whether the mesh is “watertight”.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var isWatertight: Bool { get }
```

#### Discussion

A mesh is watertight if the faces form a fully-closed volume (without gaps). A watertight mesh is required for bodies to be inflatable, and is also the reason why [`volume`](clothmeshresource/volume.md) will only return a non-nil value for watertight meshes.

If you want your body to be inflatable (by setting [`inflationConstraint`](clothbodycomponent/inflationconstraint-swift.property.md)), the body mesh needs to be watertight.

## See Also

- [var volume: Float?](clothmeshresource/volume.md)
  The volume of the mesh, or `nil` if the mesh is not watertight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/iswatertight)*