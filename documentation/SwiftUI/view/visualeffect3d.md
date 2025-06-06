# visualEffect3D(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies effects to this view, while providing access to layout information through a 3D geometry proxy.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func visualEffect3D(_ effect: @escaping (EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View
```

#### Return Value

A view with the effect applied.

#### Discussion

You return new effects by calling functions on the first argument provided to the `effect` closure. In this example, `ContentView` is offset in Z by its own depth, causing its back face to appear where the front face of the view was originally located:

```swift
ContentView()
    .visualEffect3D { content, geometryProxy in
        content.offset(z: geometryProxy.size.depth)
    }
```

## Parameters

- `effect`: A closure that returns the effect to be applied. The first   argument provided to the closure is a placeholder representing   this view. The second argument is a  .

## See Also

- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](view/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [protocol VisualEffect](visualeffect.md)
  Visual Effects change the visual appearance of a view without changing its ancestors or descendents.
- [struct EmptyVisualEffect](emptyvisualeffect.md)
  The base visual effect that you apply additional effect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/visualeffect3d(_:))*