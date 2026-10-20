# ModelSortGroup.PlanarUIPlacement

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

A set of predefined groups that indicate how the renderer draws a model relative to a planar mesh or a SwiftUI view that’s coplanar and overlapping.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum PlanarUIPlacement
```

##### Overview

Use one of the predefined groups [`planarUIInline`](./planaruiinline.md), [`planarUIAlwaysInFront`](./planaruialwaysinfront.md), and [`planarUIAlwaysBehind`](./planaruialwaysbehind.md) to order virtual content relative to coincidental (coplanar and overlapping) app UI to avoid rendering artifacts.

##### Placing virtual content relative to app UI

The scenario below shows a museum scene that has a green planar mesh entity, stacked between two SwiftUI [`View`](../../SwiftUI/view.md) instances in a [`ZStack`](../../SwiftUI/zstack.md).

| **Actual View** | **Layout Illustration** |
| --- | --- |
| ![A screenshot of a museum scene with the red UI layer drawing first, followed by the greenPlane entity drawing second, and the layer with text and symbol drawing third. All 3 are coplanar and overlapping with one another.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/modelsortgroupcomponent-planarui-green-inline-dark.jpg) | ![A screenshot illustrating the relative layout of the 3 layers in this scenario with the red UI layer at the back, greenPlane entity in the middle, and the UI with text and SF Symbol in front.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/modelsortgroupcomponent-planarui-layer-breakdown.jpg) |

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

Use the [`planarUIInline`](./planaruiinline.md) group to draw the `greenPlane` entity according to its placement within the `ZStack`. The `greenPlane` draws over the red layer, and the text/symbol draws over the `greenPlane`.

```swift
let group = ModelSortGroup.planarUIAlwaysInline
greenPlane.components.set(ModelSortGroupComponent(group: group, order: 0))
```

![A screenshot of a museum scene with the red UI layer drawing first, followed by the greenPlane entity drawing second, and the layer with text and symbol drawing third. All 3 are coplanar and overlapping with one another.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/modelsortgroupcomponent-planarui-green-inline-dark.jpg)

Use the [`planarUIAlwaysInFront`](./planaruialwaysinfront.md) group to order the `greenPlane` after both UI layers. The `greenPlane` draws over both the text/symbol layer and the red layer.

```swift
let group = ModelSortGroup.planarUIAlwaysInFront
greenPlane.components.set(ModelSortGroupComponent(group: group, order: 0))
```

![A screenshot of a museum scene with the greenPlane entity drawing after both UI layers. All 3 are coplanar and overlapping with one another.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/modelsortgroupcomponent-planarui-green-alwaysinfront-dark.jpg)

Use the [`planarUIAlwaysBehind`](./planaruialwaysbehind.md) group to order the `greenPlane` before both UI layers. The red layer and the text/symbol layer both draw over the `greenPlane`.

```swift
let group = ModelSortGroup.planarUIAlwaysBehind
greenPlane.components.set(ModelSortGroupComponent(group: group, order: 0))
```

![A screenshot of a living room scene with the greenPlane entity drawing before both UI layers. All 3 are coplanar and overlapping with one another.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/modelsortgroupcomponent-planarui-green-alwaysbehind-dark.jpg)

## Topics

### Enumeration Cases
- [ModelSortGroup.PlanarUIPlacement.alwaysBehind](./planaruiplacement-swift.enum/alwaysbehind.md)
  Instructs the renderer to draw a model’s mesh behind a SwiftUI layer that’s coincident with the mesh.
- [ModelSortGroup.PlanarUIPlacement.alwaysInFront](./planaruiplacement-swift.enum/alwaysinfront.md)
  Instructs the renderer to draw a model’s mesh in front of a SwiftUI layer that’s coincident with the mesh.
- [ModelSortGroup.PlanarUIPlacement.inlineUI](./planaruiplacement-swift.enum/inlineui.md)
  Instructs the renderer to draw a model’s mesh along with a SwiftUI layer that’s coincident with the mesh.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelsortgroup/planaruiplacement-swift.enum)*