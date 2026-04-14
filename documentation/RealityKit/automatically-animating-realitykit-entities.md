# Automatically animating RealityKit entities

**Framework**: RealityKit

Invoke implicit animations by setting the entity’s desired end state.

#### Overview

When you build 3D experiences with RealityKit, you often animate changes to an entity’s position, rotation, scale, or other properties. You can animate entity properties explicitly by creating an [`AnimationResource`](animationresource.md). RealityKit can also animate changes automatically using *implicit animations*, which let you describe only the desired end state inside a closure.

RealityKit offers two closure-based approaches to implicit animation:

- **[`animate(_:body:completion:)`](entity/animate(_:body:completion:).md)**: A type method you call directly on [`Entity`](entity.md). You pass in an [`Animation`](https://developer.apple.com/documentation/SwiftUI/Animation), and RealityKit animates any property changes you make inside the `body` closure. Use this approach when your animation doesn’t depend on SwiftUI state.
- **[`animate(body:completion:)`](realityviewcontent/animate(body:completion:).md)**: An instance method on the `content` parameter inside a [`RealityView`](realityview.md) update closure. This approach picks up the animation from the current SwiftUI transaction. You control the animation by binding it to the [`State`](https://developer.apple.com/documentation/SwiftUI/State) variable that triggers the update.

Both approaches can animate properties for the following component types:

- [`Transform`](transform.md)
- [`OpacityComponent`](opacitycomponent.md)
- [`ModelComponent`](modelcomponent.md)
- [`ParticleEmitterComponent`](particleemittercomponent.md)
- [`BillboardComponent`](billboardcomponent.md)
- [`DirectionalLightComponent`](directionallightcomponent.md)
- [`PointLightComponent`](pointlightcomponent.md)
- [`SpotLightComponent`](spotlightcomponent.md)

#### Animate Entities Without Swiftui State

Use [`animate(_:body:completion:)`](entity/animate(_:body:completion:).md) to animate entity properties without any SwiftUI state binding. Pass an [`Animation`](https://developer.apple.com/documentation/SwiftUI/Animation) value and a closure that sets the properties you want to change. RealityKit interpolates each property from its current value to the new one using the animation you specify. Often, you can get the animation you want by using one of the static type classes on [`Animation`](https://developer.apple.com/documentation/SwiftUI/Animation), like [`linear`](https://developer.apple.com/documentation/SwiftUI/Animation/linear) or [`easeOut`](https://developer.apple.com/documentation/SwiftUI/Animation/easeOut), rather than manually building a custom [`Animation`](https://developer.apple.com/documentation/SwiftUI/Animation).

The following example moves an entity to a new position over one second using a `linear` animation to give a consistent speed throughout:

```swift
Entity.animate(.linear(duration: 1.0)) {
    entity.position = SIMD3<Float>(0, 1.5, -2)
}
```

The [`animate(_:body:completion:)`](entity/animate(_:body:completion:).md) method works without a [`RealityView`](realityview.md) update closure or a SwiftUI state binding.

#### Animate Entities in a Realityview Update Closure

Use [`animate(body:completion:)`](realityviewcontent/animate(body:completion:).md) inside a [`RealityView`](realityview.md) update closure to animate entity changes in response to SwiftUI state changes. Because this method derives its animation from the current SwiftUI transaction, attach an animation to the [`State`](https://developer.apple.com/documentation/SwiftUI/State) variable that triggers the update.

Bind the animation to your state variable using the [`animation(_:)`](https://developer.apple.com/documentation/SwiftUI/Binding/animation(_:)) modifier on a [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding).

```swift
@State private var isScaled = false

var body: some View {
    VStack {
        RealityView { content in
            // Add entities during initial setup.
        } update: { content in
            guard let entity = content.entities.first else { return }

            content.animate {
                if isScaled {
                    entity.components[Transform.self]?.scale = SIMD3<Float>(repeating: 2)
                } else {
                    entity.components[Transform.self]?.scale = SIMD3<Float>(repeating: 1)
                }
            }
        }

        Toggle("Scale", isOn: $isScaled.animation(.linear(duration: 1.0)))
    }
}
```

The `.animation(.linear(duration: 1.0))` modifier on `$isScaled` attaches an animation to the binding. When `isScaled` changes, [`RealityView`](realityview.md) calls the update closure within a transaction that carries this animation. The [`animate(body:completion:)`](realityviewcontent/animate(body:completion:).md) call applies that animation to the property changes inside the closure.

> ❗ **Important**: Call [`animate(body:completion:)`](realityviewcontent/animate(body:completion:).md) only inside the update closure, not the make closure. The method relies on a SwiftUI transaction, which is only available during an update pass. Calling it during initial setup has no effect and logs a fault.

#### Animate Multiple Properties

You can change multiple properties inside a single `animate` closure. RealityKit creates a separate animation for each property and drives them all with the same timing.

The following example animates an entity’s position, scale, and opacity at the same time:

```swift
Entity.animate(.easeInOut(duration: 1.5)) {
    entity.components[Transform.self]?.translation = SIMD3<Float>(0, 2, -3)
    entity.components[Transform.self]?.scale = SIMD3<Float>(repeating: 1.5)
    entity.components[OpacityComponent.self]?.opacity = 0.5
}
```

> ❗ **Important**: When you animate [`Transform`](transform.md) properties, set them together through `entity.components[Transform.self]` rather than setting [`position`](hastransform/position.md), [`scale`](hastransform/scale.md), and [`orientation`](hastransform/orientation.md) individually. Setting these convenience properties separately inside the closure generates independent animations that conflict, producing unexpected results.

#### Respond to Animation Completion

Both [`animate(_:body:completion:)`](entity/animate(_:body:completion:).md) and [`animate(body:completion:)`](realityviewcontent/animate(body:completion:).md) accept an optional `completion` closure. RealityKit calls this closure when the animation finishes. The completion closure also runs if a new animation begins on the same property before the current animation finishes.

Use the completion handler to chain animations or trigger follow-up logic. The following code example moves the entity to a new position, and the completion handler moves the entity back to the origin:

```swift
Entity.animate(.easeIn(duration: 0.8)) {
    entity.components[Transform.self]?.translation = SIMD3<Float>(0, 1.5, -2)
} completion: {
    Entity.animate(.easeOut(duration: 0.8)) {
        entity.components[Transform.self]?.translation = .zero
    }
}
```

## See Also

- [class AnimationResource](animationresource.md)
  An animation for the properties of scenes or entities.
- [struct AnimationLibraryComponent](animationlibrarycomponent.md)
  A component that represents a collection of animations that an entity can play.
- [AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animationcollection.md)
  A collection of animations an entity can play.
- [enum AnimationEvents](animationevents.md)
  Notable milestones that the framework signals during animation playback.
- [class AnimationPlaybackController](animationplaybackcontroller.md)
  A controller that manages animation playback.
- [enum AnimationRepeatMode](animationrepeatmode.md)
  Options that determine whether an animation replays after completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/automatically-animating-realitykit-entities)*