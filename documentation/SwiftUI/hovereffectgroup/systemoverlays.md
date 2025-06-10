# systemOverlays

**Framework**: SwiftUI  
**Kind**: property

A `HoverEffectGroup` that becomes active when system overlays are visible.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var systemOverlays: HoverEffectGroup { get }
```

#### Discussion

Use this group to synchronize effects with system overlays. In the following example, the back button will be hidden whenever system overlays are hidden.

```swift
Button("Back") { }
    .hoverEffect(in: .systemOverlays) { e, isActive, _ in
        e.animation(
            isActive ? .systemOverlayAppearance : .systemOverlayDelayedDisappearance
        ) {
            $0.opacity(isActive ? 1 : 0)
        }
    }
    .persistentSystemOverlays(.hidden)
```

This example uses the `systemOverlayAppearance` and `systemOverlayDisappearance` animations to ensure the effect using the same timing as system overlays.

If `persistentSystemOverlays` is not `.hidden`, this group will always be active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectgroup/systemoverlays)*