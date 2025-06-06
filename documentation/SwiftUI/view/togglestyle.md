# toggleStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for toggles in a view hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func toggleStyle<S>(_ style: S) -> some View where S : ToggleStyle
```

#### Return Value

A view that uses the specified toggle style for itself and its child views.

#### Discussion

Use this modifier on a [`Toggle`](toggle.md) instance to set a style that defines the control’s appearance and behavior. For example, you can choose the [`switch`](togglestyle/switch.md) style:

```swift
Toggle("Vibrate on Ring", isOn: $vibrateOnRing)
    .toggleStyle(.switch)
```

Built-in styles typically have a similar appearance across platforms, tailored to the platform’s overall style:

| Platform | Appearance |
| --- | --- |
| iOS, iPadOS | ![A screenshot of the text Vibrate on Ring appearing to the left of a toggle switch that’s on. The toggle’s tint color is green. The toggle and its text appear in a rounded rectangle.](https://docs-assets.developer.apple.com/published/90deb976984567d835517e64555ce986/View-toggleStyle-1-iOS%402x.png) |
| macOS | ![A screenshot of the text Vibrate on Ring appearing to the left of a toggle switch that’s on. The toggle’s tint color is blue. The toggle and its text appear on a neutral background.](https://docs-assets.developer.apple.com/published/1cd62d0dec90241bf316800b28e25862/View-toggleStyle-1-macOS%402x.png) |

##### Styling Toggles in a Hierarchy

You can set a style for all toggle instances within a view hierarchy by applying the style modifier to a container view. For example, you can apply the [`button`](togglestyle/button.md) style to an [`HStack`](hstack.md):

```swift
HStack {
    Toggle(isOn: $isFlagged) {
        Label("Flag", systemImage: "flag.fill")
    }
    Toggle(isOn: $isMuted) {
        Label("Mute", systemImage: "speaker.slash.fill")
    }
}
.toggleStyle(.button)
```

The example above has the following appearance when `isFlagged` is `true` and `isMuted` is `false`:

| Platform | Appearance |
| --- | --- |
| iOS, iPadOS | ![A screenshot of two buttons arranged horizontally. The first has the image of a flag and is active with a blue tint. The second has an image of a speaker with a line through it and is inactive with a neutral tint.](https://docs-assets.developer.apple.com/published/041f6e83a5670d01f46a9d234a74bd59/View-toggleStyle-2-iOS%402x.png) |
| macOS | ![A screenshot of two buttons arranged horizontally. The first has the image of a flag and is active with a blue tint. The second has an image of a speaker with a line through it and is inactive with a neutral tint.](https://docs-assets.developer.apple.com/published/44a1adcdab9ae2e9b542d17fea64c41c/View-toggleStyle-2-macOS%402x.png) |

##### Automatic Styling

If you don’t set a style, SwiftUI assumes a value of [`automatic`](togglestyle/automatic.md), which corresponds to a context-specific default. Specify the automatic style explicitly to override a container’s style and revert to the default:

```swift
HStack {
    Toggle(isOn: $isShuffling) {
        Label("Shuffle", systemImage: "shuffle")
    }
    Toggle(isOn: $isRepeating) {
        Label("Repeat", systemImage: "repeat")
    }

    Divider()

    Toggle("Enhance Sound", isOn: $isEnhanced)
        .toggleStyle(.automatic) // Revert to the default style.
}
.toggleStyle(.button) // Use button style for toggles in the stack.
.labelStyle(.iconOnly) // Omit the title from any labels.
```

The style that SwiftUI uses as the default depends on both the platform and the context. In macOS, the default in most contexts is a [`checkbox`](togglestyle/checkbox.md), while in iOS, the default toggle style is a [`switch`](togglestyle/switch.md):

| Platform | Appearance |
| --- | --- |
| iOS, iPadOS | ![A screenshot of several horizontally arranged items: two buttons, a vertical divider line, the text Enhance sound, and a switch. The first button has two right facing arrows that cross over in the middle and is active with a blue tint. The second button has one right and one left facing arrow and is inactive with neutral tint. The switch is on and has a green tint.](https://docs-assets.developer.apple.com/published/713a018359ab9ecdfe222029b7a2366a/View-toggleStyle-3-iOS%402x.png) |
| macOS | ![A screenshot of several horizontally arranged items: two buttons, a vertical divider line, a checkbox, and the text Enhance sound. The first button has two right facing arrows that cross over in the middle and is active with a blue tint. The second button has one right and one left facing arrow and is inactive with a neutral tint. The check box is checked and has a blue tint.](https://docs-assets.developer.apple.com/published/7348c954c3ccc51b7cf2057fa69f660a/View-toggleStyle-3-macOS%402x.png) |

> **Note**: Like toggle style does for toggles, the [`labelStyle(_:)`](view/labelstyle(_:).md) modifier sets the style for [`Label`](label.md) instances in the hierarchy. The example above demostrates the compact [`iconOnly`](labelstyle/icononly.md) style, which is useful for button toggles in space-constrained contexts. Always include a descriptive title for better accessibility.

Like toggle style does for toggles, the [`labelStyle(_:)`](view/labelstyle(_:).md) modifier sets the style for [`Label`](label.md) instances in the hierarchy. The example above demostrates the compact [`iconOnly`](labelstyle/icononly.md) style, which is useful for button toggles in space-constrained contexts. Always include a descriptive title for better accessibility.

For more information about how SwiftUI chooses a default toggle style, see the [`automatic`](togglestyle/automatic.md) style.

## Parameters

- `style`: The toggle style to set. Use one of the built-in   values, like   or  ,   or a custom style that you define by creating a type that conforms   to the   protocol.

## See Also

- [struct Slider](slider.md)
  A control for selecting a value from a bounded linear range of values.
- [struct Stepper](stepper.md)
  A control that performs increment and decrement actions.
- [struct Toggle](toggle.md)
  A control that toggles between on and off states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/togglestyle(_:))*