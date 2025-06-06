# accessibilityRepresentation(representation:)

**Framework**: SwiftUI  
**Kind**: method

Replaces one or more accessibility elements for this view with new accessibility elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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

You can make controls accessible by using a custom style. For example, a custom [`ToggleStyle`](togglestyle.md) that you create inherits the accessibility features of [`Toggle`](toggle.md) automatically. When you can’t use the parent view’s accessibility elements, use the `accessibilityRepresentation(representation:)` modifier instead. This modifier replaces default accessibility elements with different accessibility elements that you provide. You use synthetic, non-visual accessibility elements to represent what the view displays.

The example below makes a custom adjustable control accessible by explicitly defining the representation of its step increments using a [`Slider`](slider.md):

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

## See Also

- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](view/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the [`AccessibilityChildBehavior`](accessibilitychildbehavior.md) of the existing accessibility element.
- [func accessibilityChildren<V>(children: () -> V) -> some View](view/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [struct AccessibilityChildBehavior](accessibilitychildbehavior.md)
  Defines the behavior for the child elements of the new parent element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityrepresentation(representation:))*