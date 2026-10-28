# tint(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the tint within this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func tint<S>(_ tint: S?) -> some View where S : ShapeStyle
```

**Other overloads**:

```swift
nonisolated
func tint(_ tint: Color?) -> some View
```

## Discussion

Use this method to override the default accent color for this view with a given styling. Unlike an app’s accent color, which can be overridden by user preference, tint is always respected and should be used as a way to provide additional meaning to the control.

Controls which are unable to style themselves using the given type of `ShapeStyle` will try to approximate the styling as best as they can (i.e. controls which can not style themselves using a gradient will attempt to use the color of the gradient’s first stop).

This example shows a linear gauge tinted with a gradient from [`blue`](../shapestyle/blue.md) to [`red`](../shapestyle/red.md).

```swift
struct ControlTint: View {
    var body: some View {
        Gauge(value: 75, in: 0...100) {
            Text("Temperature")
        }
        .gaugeStyle(.linearCapacity)
        .tint(Gradient(colors: [.blue, .orange, .red]))
    }
}
```

Some controls adapt to the tint color differently based on their style, the current platform, and the surrounding context. For example, in macOS, a button with the [`bordered`](../primitivebuttonstyle/bordered.md) style doesn’t tint its background, but one with the [`borderedProminent`](../primitivebuttonstyle/borderedprominent.md) style does. In macOS, neither of these button styles tint their label, but they do in other platforms.

## Parameters

- `tint`: The tint to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tint(_:)-93mfq)*