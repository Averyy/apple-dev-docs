# selection

**Framework**: SwiftUI  
**Kind**: property

A style used to visually indicate selection following platform conventional colors and behaviors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static var selection: SelectionShapeStyle { get }
```

#### Discussion

For example:

```swift
ForEach(items) {
   ItemView(value: item, isSelected: item.id == selectedID)
}

struct ItemView {
    var value: item
    var isSelected: Bool

    var body: some View {
        // construct the actual cell content
            .background(isSelected
                ? AnyShapeStyle(.selection)
                    : AnyShapeStyle(.fill.quaternary),
                in: .rect(cornerRadius: 6))
    }
}
```

On macOS and iPadOS this automatically reflects window key state and focus state, where the emphasized appearance will be used only when the window is key and the nearest focusable element is actually focused. On iPhone, this will always fill with the environment’s accent color.

When applied as a background of another view, it will automatically set the `EnvironmentValues.backgroundProminence` for the environment of that view to match the current prominence of the selection.

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [static var foreground: ForegroundStyle](shapestyle/foreground.md)
  The foreground style in the current context.
- [static var background: BackgroundStyle](shapestyle/background.md)
  The background style in the current context.
- [static var separator: SeparatorShapeStyle](shapestyle/separator.md)
  A style appropriate for foreground separator or border lines.
- [static var tint: TintShapeStyle](shapestyle/tint.md)
  A style that reflects the current tint color.
- [static var placeholder: PlaceholderTextShapeStyle](shapestyle/placeholder.md)
  A style appropriate for placeholder text.
- [static var link: LinkShapeStyle](shapestyle/link.md)
  A style appropriate for links.
- [static var fill: FillShapeStyle](shapestyle/fill.md)
  An overlay fill style for filling shapes.
- [static var windowBackground: WindowBackgroundShapeStyle](shapestyle/windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/selection)*