# Applying Liquid Glass to custom views

**Framework**: SwiftUI

Configure, combine, and morph views using Liquid Glass effects.

#### Overview

Interfaces across Apple platforms feature a new dynamic material called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. Liquid Glass is a material that blurs content behind it, reflects color and light of surrounding content, and reacts to touch and pointer interactions in real time. Standard components in SwiftUI use Liquid Glass. Adopt Liquid Glass on custom components to move, combine, and morph them into one another with unique animations and transitions.

![An image of the Landmarks sample code on iPad, in landscape, showing the Mount Fuji landmark.](https://docs-assets.developer.apple.com/published/86bea3b2d851de88291e52e7845ef990/liquid-glass-landmarks-hero%402x.png)

To learn about Liquid Glass and more, see [`Landmarks: Building an app with Liquid Glass`](landmarks-building-an-app-with-liquid-glass.md).

#### Apply and Configure Liquid Glass Effects

Use the [`glassEffect(_:in:isEnabled:)`](view/glasseffect(_:in:isenabled:).md) modifier to add Liquid Glass effects to a view. By default, the modifier uses the [`regular`](glass/regular.md) variant of [`Glass`](glass.md) and applies the given effect within a [`Capsule`](capsule.md) shape behind the view’s content.

Configure the effect to customize your components in a variety of ways:

- Use different shapes to have a consistent look and feel across custom components in your app. For example, use a rounded rectangle if you’re applying the effect to larger components that would look odd as a `Capsule` or [`Circle`](circle.md).
- Define a tint color to suggest prominence.
- Add [`interactive(_:)`](glass/interactive(_:).md) to custom components to make them react to touch and pointer interactions. This applies the same responsive and fluid reactions that [`glass`](primitivebuttonstyle/glass.md) provides to standard buttons.

In the examples below, observe how to apply Liquid Glass effects to a view, use an alternate shape with a specific corner radius, and create a tinted view that responds to interactivity:

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()

Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect(in: .rect(cornerRadius: 16.0))

Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect(.regular.tint(.orange).interactive())
```

#### Combine Multiple Views with Liquid Glass Containers

Use [`GlassEffectContainer`](glasseffectcontainer.md) when applying Liquid Glass effects on multiple views to achieve the best rendering performance. A container also allows views with Liquid Glass effects to blend their shapes together and to morph in and out of each other during transitions. Inside a container, each view with the [`glassEffect(_:in:isEnabled:)`](view/glasseffect(_:in:isenabled:).md) modifier renders with the effects behind it.

Customize the spacing on the container to set layout spacing between views and to affect how the Liquid Glass effects behind views interact with one another. Views close to one another merge their effects into a single shape. The farther views are from each other, the sooner the shapes merge into each other.

The `.glassEffect()` modifier captures the content to send to the container to render. Apply the `.glassEffect()` modifier after other modifiers that will affect the appearance of the view.

In the example below, two images are placed close to each other and the Liquid Glass effects begin to blend their shapes together. This creates a fluid animation as components move around each other within a container:

![Two Image views representing a scribble symbol on the left, and an eraser symbol on the right. The views are close to each other, which causes the Liquid Glass effects to merge the views.](https://docs-assets.developer.apple.com/published/1a45d9481869becc2c40374ece262425/liquid-glass-joined-view%402x.png)

```swift
GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()

        Image(systemName: "eraser.fill")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()

            // An `offset` shows how Liquid Glass effects react to each other in a container.
            // Use animations and components appearing and disappearing to obtain effects that look purposeful.
            .offset(x: -40.0, y: 0.0)
    }
}
```

In some cases, you want the geometries of multiple views to contribute to a single Liquid Glass effect capsule, even when your content is at rest. Use the [`glassEffectUnion(id:namespace:)`](view/glasseffectunion(id:namespace:).md) modifier to specify that a view contributes to a united effect with a particular ID. This combines all effects with a similar shape, Liquid Glass effect, and ID into a single shape with the applied Liquid Glass material. This is especially useful when creating views dynamically, or with views that live outside of an [`HStack`](hstack.md) or [`VStack`](vstack.md).

![Four Image views that have Liquid Glass effects applied. A rain cloud with lightning symbol and a sun with rain symbol have a unioned Liquid Glass effect encapsulating both of them, followed by a unioned Liquid Glass effect of a moon with stars symbol and a moon symbol.](https://docs-assets.developer.apple.com/published/4426e68642783951fe56b1d7485825cc/liquid-glass-unioned-views%402x.png)

```swift
let symbolSet: [String] = ["cloud.bolt.rain.fill", "sun.rain.fill", "moon.stars.fill", "moon.fill"]

GlassEffectContainer(spacing: 20.0) {
    HStack(spacing: 20.0) {
        ForEach(symbolSet.indices, id: \.self) { item in
            Image(systemName: symbolSet[item])
                .frame(width: 80.0, height: 80.0)
                .font(.system(size: 36))
                .glassEffect()
                .glassEffectUnion(id: item < 2 ? "1" : "2", namespace: namespace)
        }
    }
}
```

#### Morph Liquid Glass Effects During Transitions

Morphing effects occur during transitions between views with Liquid Glass effects. Add these transitions to views with effects in a container by using the [`glassEffectID(_:in:)`](view/glasseffectid(_:in:).md) modifier.

Associate each Liquid Glass effect with a unique identifier within a namespace the [`Namespace`](namespace.md) property wrapper provides. These IDs ensure SwiftUI animates the same shapes correctly when a shape appears or disappears due to view hierarchy changes. SwiftUI uses the spacing provided to the effect container along with the geometry of the shapes themselves to determine appropriate shapes to morph into and out of.

In the example below, the eraser image transitions into and out of the pencil image when the `isExpanded` variable changes. The `GlassEffectContainer` has a spacing value of `40.0`, and the `HStack` within it has a spacing of `40.0`. This morphs the eraser image into the pencil image when the eraser’s nearest edge is less than or equal to the container’s spacing.

```swift
@State private var isExpanded: Bool = false
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 40.0) {
        HStack(spacing: 40.0) {
            Image(systemName: "scribble.variable")
                .frame(width: 80.0, height: 80.0)
                .font(.system(size: 36))
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

            if isExpanded {
                Image(systemName: "eraser.fill")
                    .frame(width: 80.0, height: 80.0)
                    .font(.system(size: 36))
                    .glassEffect()
                    .glassEffectID("eraser", in: namespace)
            }
        }
    }

    Button("Toggle") {
        withAnimation {
            isExpanded.toggle()
        }
    }
    .buttonStyle(.glass)
}
```

## See Also

- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md)
  Enhance your app experience with system-provided and custom Liquid Glass.
- [func glassEffect(Glass, in: some Shape, isEnabled: Bool) -> some View](view/glasseffect(_:in:isenabled:).md)
  Applies the Liquid Glass effect to a view.
- [func interactive(Bool) -> Glass](glass/interactive(_:).md)
  Returns a copy of the structure configured to be interactive.
- [struct GlassEffectContainer](glasseffectcontainer.md)
  A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [struct GlassEffectTransition](glasseffecttransition.md)
  A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [struct GlassButtonStyle](glassbuttonstyle.md)
  A button style that applies glass border artwork based on the button’s context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views)*