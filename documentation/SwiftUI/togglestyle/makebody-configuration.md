# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a toggle.

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
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Return Value

A view that has behavior and appearance that enables it to function as a [`Toggle`](toggle.md).

#### Discussion

Implement this method when you define a custom toggle style that conforms to the [`ToggleStyle`](togglestyle.md) protocol. Use the `configuration` input — a [`ToggleStyleConfiguration`](togglestyleconfiguration.md) instance — to access the toggle’s label and state. Return a view that has the appearance and behavior of a toggle. For example you can create a toggle that displays a label and a circle that’s either empty or filled with a checkmark:

```swift
struct ChecklistToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Button {
            configuration.isOn.toggle()
        } label: {
            HStack {
                Image(systemName: configuration.isOn
                        ? "checkmark.circle.fill"
                        : "circle")
                configuration.label
            }
        }
        .tint(.primary)
        .buttonStyle(.borderless)
    }
}
```

The `ChecklistToggleStyle` toggle style provides a way to both observe and modify the toggle state: the circle fills for the on state, and users can tap or click the toggle to change the state. By using a customized [`Button`](button.md) to compose the toggle’s body, SwiftUI automatically provides the behaviors that users expect from a control that has button-like characteristics.

You can present a collection of toggles that use this style in a stack:

![A screenshot of three items stacked vertically. All have a circle](https://docs-assets.developer.apple.com/published/9b7fe9eb8c503266cef0989aaa76b4f2/ToggleStyle-makeBody-1-iOS%402x.png)

When updating a view hierarchy, the system calls your implementation of the `makeBody(configuration:)` method for each [`Toggle`](toggle.md) instance that uses the associated style.

##### Modify the Current Style

Rather than create an entirely new style, you can alternatively modify a toggle’s current style. Use the [`init(_:)`](toggle/init(_:).md) initializer inside the `makeBody(configuration:)` method to create and modify a toggle based on a `configuration` value. For example, you can create a style that adds padding and a red border to the current style:

```swift
struct RedBorderToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Toggle(configuration)
            .padding()
            .border(.red)
    }
}
```

If you create a `redBorder` static variable from this style, you can apply the style to toggles that already use another style, like the built-in [`switch`](togglestyle/switch.md) and [`button`](togglestyle/button.md) styles:

```swift
Toggle("Switch", isOn: $isSwitchOn)
    .toggleStyle(.redBorder)
    .toggleStyle(.switch)

Toggle("Button", isOn: $isButtonOn)
    .toggleStyle(.redBorder)
    .toggleStyle(.button)
```

Both toggles appear with the usual styling, each with a red border:

![A screenshot of a switch toggle with a red border, and a button](https://docs-assets.developer.apple.com/published/ee962c276c8f7fe7def8e6accfb25adc/ToggleStyle-makeBody-2-iOS%402x.png)

Apply the custom style closer to the toggle than the modified style because SwiftUI evaluates style view modifiers in order from outermost to innermost. If you apply the styles in the other order, the red border style doesn’t have an effect, because the built-in styles override it completely.

## Parameters

- `configuration`: The properties of the toggle, including a   label and a binding to the toggle’s state.

## See Also

- [struct ToggleStyleConfiguration](togglestyleconfiguration.md)
  The properties of a toggle instance.
- [ToggleStyle.Configuration](togglestyle/configuration.md)
  The properties of a toggle instance.
- [associatedtype Body : View](togglestyle/body.md)
  A view that represents the appearance and interaction of a toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyle/makebody(configuration:))*