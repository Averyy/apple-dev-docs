# animation(_:body:)

**Framework**: SwiftUI  
**Kind**: method

Applies the given [`Animation`](animation.md) to all effects within the `body` closure.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func animation(_ animation: Animation?, body: (EmptyHoverEffectContent) -> some HoverEffectContent) -> some HoverEffectContent
```

#### Return Value

A new effect that combines the effects defined in `body` with

#### Discussion

Any effects defined within the `body` closure will be combined with this effect, and the `animation` will used to animate those effects’ changes when the effects are applied.

In the following example, the view will use the `.easeIn` animation when activating the effect, but `.easeOut` when the effect becomes inactive:

```swift
Color.red
    .hoverEffect { effect, isActive, proxy in
        effect.animation(isActive ? .easeIn : .easeOut) {
            $0.opacity(isActive ? 1 : 0.5)
        }
    }
```

## Parameters

- `animation`: The animation to use for the effect transition. If    the effects will not animate.
- `body`: A block used to specify the effects to animate. You must use   the provided content to build the effects, or behavior is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectcontent/animation(_:body:))*