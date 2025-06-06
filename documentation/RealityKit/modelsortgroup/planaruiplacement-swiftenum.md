# ModelSortGroup.PlanarUIPlacement

**Framework**: RealityKit  
**Kind**: enum

A set of predefined groups that indicate how the renderer draws a model relative to a planar mesh or a SwiftUI view that’s coplanar and overlapping.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum PlanarUIPlacement
```

##### Overview

Use one of the predefined groups [`planarUIInline`](modelsortgroup/planaruiinline.md), [`planarUIAlwaysInFront`](modelsortgroup/planaruialwaysinfront.md), and [`planarUIAlwaysBehind`](modelsortgroup/planaruialwaysbehind.md) to order virtual content relative to coincidental (coplanar and overlapping) app UI to avoid rendering artifacts.

##### Placing Virtual Content Relative to App Ui

The scenario below shows a museum scene that has a green planar mesh entity, stacked between two SwiftUI [`View`](https://developer.apple.com/documentation/SwiftUI/View) instances in a [`ZStack`](https://developer.apple.com/documentation/SwiftUI/ZStack).

|  |  |
| --- | --- |
| ![A screenshot of a museum scene with the red UI layer drawing first, followed by the greenPlane entity drawing second, and the layer with text and symbol drawing third. All 3 are coplanar and overlapping with one another.](https://docs-assets.developer.apple.com/published/4edf2a53d85de8fb8bed0e9a9794b2e6/modelsortgroupcomponent-planarui-green-inline-dark.jpg) | ![A screenshot illustrating the relative layout of the 3 layers in this scenario with the red UI layer at the back, greenPlane entity in the middle, and the UI with text and SF Symbol in front.](https://docs-assets.developer.apple.com/published/983f602fa7218629e360047efa5e2010/modelsortgroupcomponent-planarui-layer-breakdown.jpg) |

```swift
ZStack {
   // A red UI layer.
   Color(.red).opacity(0.5)
       .frame(width: 700, height: 520, alignment: .center)
       .clipShape(RoundedRectangle(cornerRadius: 40))

   // A green plane with 0.9 opacity.
   RealityView { content in
       let greenPlane = Entity()
       let planeModel = ModelComponent(
           mesh: .generatePlane(width: 0.3, height: 0.2, cornerRadius: 0.01),
           materials: [UnlitMaterial(color: .green)]
       )
       greenPlane.components.set(planeModel)
       greenPlane.components.set(OpacityComponent(opacity: 0.9))

       // Set the model sort group to planarUIInline.
       let group = ModelSortGroup.planarUIInline
       greenPlane.components.set(ModelSortGroupComponent(group: group, order: 0))
       content.add(greenPlane)
   }
   .frame(depth: 0.0)

   // A UI with text and SF symbol.
   VStack {
       Text("Hello World").font(.system(size: 50))
       Image(systemName: "visionpro")
           .resizable()
           .foregroundColor(.yellow)
           .aspectRatio(contentMode: .fit)
           .frame(width: 80.0, height: 80.0)
   }
   .frame(width: 460, height: 240, alignment: .center)
   .offset(z: .ulpOfOne)
}
```

Use the [`planarUIInline`](modelsortgroup/planaruiinline.md) group to draw the `greenPlane` entity according to its placement within the `ZStack`. The `greenPlane` draws over the red layer, and the text/symbol draws over the `greenPlane`.

```swift
let group = ModelSortGroup.planarUIAlwaysInline
greenPlane.components.set(ModelSortGroupComponent(group: group, order: 0))
```

Use the [`planarUIAlwaysInFront`](modelsortgroup/planaruialwaysinfront.md) group to order the `greenPlane` after both UI layers. The `greenPlane` draws over both the text/symbol layer and the red layer.

```swift
let group = ModelSortGroup.planarUIAlwaysInFront
greenPlane.components.set(ModelSortGroupComponent(group: group, order: 0))
```

Use the [`planarUIAlwaysBehind`](modelsortgroup/planaruialwaysbehind.md) group to order the `greenPlane` before both UI layers. The red layer and the text/symbol layer both draw over the `greenPlane`.

```swift
let group = ModelSortGroup.planarUIAlwaysBehind
greenPlane.components.set(ModelSortGroupComponent(group: group, order: 0))
```

## Topics

### Operators
- [static func == (ModelSortGroup.PlanarUIPlacement, ModelSortGroup.PlanarUIPlacement) -> Bool](modelsortgroup/planaruiplacement-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ModelSortGroup.PlanarUIPlacement.alwaysBehind](modelsortgroup/planaruiplacement-swift.enum/alwaysbehind.md)
  Instructs the renderer to draw a model’s mesh behind a SwiftUI layer that’s coincident with the mesh.
- [ModelSortGroup.PlanarUIPlacement.alwaysInFront](modelsortgroup/planaruiplacement-swift.enum/alwaysinfront.md)
  Instructs the renderer to draw a model’s mesh in front of a SwiftUI layer that’s coincident with the mesh.
- [ModelSortGroup.PlanarUIPlacement.inlineUI](modelsortgroup/planaruiplacement-swift.enum/inlineui.md)
  Instructs the renderer to draw a model’s mesh along with a SwiftUI layer that’s coincident with the mesh.
### Instance Properties
- [var hashValue: Int](modelsortgroup/planaruiplacement-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](modelsortgroup/planaruiplacement-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](modelsortgroup/planaruiplacement-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelsortgroup/planaruiplacement-swift.enum)*