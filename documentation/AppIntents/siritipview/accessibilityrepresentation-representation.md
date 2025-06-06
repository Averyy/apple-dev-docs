# accessibilityRepresentation(representation:)

**Framework**: App Intents  
**Kind**: method

Replaces one or more accessibility elements for this view with new accessibility elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityRepresentation<V>(@ViewBuilder representation: () -> V) -> some View where V : View
```

#### Discussion

You can make controls accessible by using a custom style. For example, a custom `ToggleStyle` that you create inherits the accessibility features of `Toggle` automatically. When you can’t use the parent view’s accessibility elements, use the `accessibilityRepresentation(representation:)` modifier instead. This modifier replaces default accessibility elements with different accessibility elements that you provide. You use synthetic, non-visual accessibility elements to represent what the view displays.

The example below makes a custom adjustable control accessible by explicitly defining the representation of its step increments using a `Slider`:

```swift
var body: some View {
    VStack {
        SliderTrack(...) // Custom slider implementation.
    }
    .accessibilityRepresentation {
        Slider(value: $value, in: 0...100) {
            Text("Label")
        }
    }
}
```

SwiftUI hides the view that you provide in the `representation` closure and makes it non-interactive. The framework uses it only to generate accessibility elements.

## Parameters

- `representation`: A hidden view that the accessibility   system uses to generate accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilityrepresentation(representation:))*