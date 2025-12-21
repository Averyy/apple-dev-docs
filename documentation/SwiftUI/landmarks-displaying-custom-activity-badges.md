# Landmarks: Displaying custom activity badges

**Framework**: SwiftUI

Provide people with a way to mark their adventures by displaying animated custom activity badges.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- Xcode 26.0+

#### Overview

The Landmarks app lets people track their adventures as they explore sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to mark their adventures and receive custom activity badges along the way.

![An image of the landmarks view on an iPhone, with the badges view visible over some landmarks.](https://docs-assets.developer.apple.com/published/0906c5ecab4688f18b19faf293acb363/Landmarks-Building-an-app-with-Liquid-Glass-5%402x.png)

This sample displays the badges in a vertical view that includes a toggle button for showing or hiding the badges. The Landmarks app includes a custom modifier that makes it easier for other views to adopt the badge view. By configuring the badges to use Liquid Glass, the badges gain the advantage of using the morphing animation when you show or hide the badges.

#### Add a Modifier to Show Badges in Other Views

To make the badges available in other views, like `CollectionsView`, the sample uses a custom modifier, `ShowBadgesViewModifier`, as a [`ViewModifier`](viewmodifier.md). The sample layers the badges over another view using a [`ZStack`](zstack.md), and positions the badge view in the lower trailing corner:

```swift
private struct ShowsBadgesViewModifier: ViewModifier {
    func body(content: Content) -> some View {
        ZStack {
            content
            HStack {
                Spacer()
                VStack {
                    Spacer()
                    BadgesView()
                        .padding()
                }
            }
        }
    }
}
```

The sample extends [`View`](view.md) by adding the `showBadges` modifier:

```swift
extension View {
    func showsBadges() -> some View {
        modifier(ShowsBadgesViewModifier())
    }
}
```

#### Apply Liquid Glass to the Toggle Button

To create the toggle button, the sample configures a [`Button`](button.md) using `ToggleBadgesLabel` which has different system images for the Show and Hide toggle states. To apply Liquid Glass, style the button with the [`glass`](primitivebuttonstyle/glass.md) modifier:

```swift
Button {
    //...
} label: {
    //...
}
.buttonStyle(.glass)

```

#### Add Liquid Glass to the Badges

To add Liquid Glass to each badge, the sample uses the [`glassEffect(_:in:)`](view/glasseffect(_:in:).md) modifier. To make a custom glass view appearance, the sample specifies a rectangular option with a corner radius:

```swift
BadgeLabel(badge: $0)
    .glassEffect(.regular, in: .rect(cornerRadius: Constants.badgeCornerRadius))
```

#### Animate the Badges Using the Morph Effect

The morph effect is an animation for Liquid Glass views. During this animation, the toggle button and each badge start as a combined view. Then, the button and badges change shape like a liquid as they separate and move from one location to another. In reverse, the toggle button and badges change shape and combine back into one view.

To achieve the Liquid Glass morph effect, the app:

- organizes the badges and toggle button into a [`GlassEffectContainer`](glasseffectcontainer.md)
- adds [`glassEffectID(_:in:)`](view/glasseffectid(_:in:).md) to each badge
- adds [`glassEffectID(_:in:)`](view/glasseffectid(_:in:).md) to the toggle button
- wraps the command that toggles the `isExpanded` property in [`withAnimation(_:_:)`](withanimation(_:_:).md)

```swift
// Organizes the badges and toggle button to animate together.
GlassEffectContainer(spacing: Constants.badgeGlassSpacing) {
    VStack(alignment: .center, spacing: Constants.badgeButtonTopSpacing) {
        if isExpanded {
            VStack(spacing: Constants.badgeSpacing) {
                ForEach(modelData.earnedBadges) {
                    BadgeLabel(badge: $0)
                        // Adds Liquid Glass to the badge.
                        .glassEffect(.regular, in: .rect(cornerRadius: Constants.badgeCornerRadius))
                        // Adds an identifier to the badge for animation.
                        .glassEffectID($0.id, in: namespace)
                }
            }
        }

        Button {
            // Animates this button and badges when `isExpanded` changes values.
            withAnimation {
                isExpanded.toggle()
            }
        } label: {
            ToggleBadgesLabel(isExpanded: isExpanded)
                .frame(width: Constants.badgeShowHideButtonWidth,
                       height: Constants.badgeShowHideButtonHeight)
        }
        // Adds Liquid Glass to the button.
        .buttonStyle(.glass)
        #if os(macOS)
        .tint(.clear)
        #endif
        // Adds an identifier to the button for animation.
        .glassEffectID("togglebutton", in: namespace)
    }
    .frame(width: Constants.badgeFrameWidth)
}
```

## See Also

- [Landmarks: Applying a background extension effect](landmarks-applying-a-background-extension-effect.md)
  Configure an image to blur and extend under a sidebar or inspector panel.
- [Landmarks: Extending horizontal scrolling under a sidebar or inspector](landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector.md)
  Improve your horizontal scrollbar’s appearance by extending it under a sidebar or inspector.
- [Landmarks: Refining the system provided Liquid Glass effect in toolbars](landmarks-refining-the-system-provided-glass-effect-in-toolbars.md)
  Organize toolbars into related groupings to improve their appearance and utility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/landmarks-displaying-custom-activity-badges)*