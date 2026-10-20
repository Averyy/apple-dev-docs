# selection

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A style used to visually indicate selection following platform conventional colors and behaviors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var selection: SelectionShapeStyle { get }
```

Available when `Self` is `SelectionShapeStyle`.

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

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Semantic styles
- [static var foreground: ForegroundStyle](./foreground.md)
  The foreground style in the current context.
- [static var background: BackgroundStyle](./background.md)
  The background style in the current context.
- [static var separator: SeparatorShapeStyle](./separator.md)
  A style appropriate for foreground separator or border lines.
- [static var tint: TintShapeStyle](./tint.md)
  A style that reflects the current tint color.
- [static var placeholder: PlaceholderTextShapeStyle](./placeholder.md)
  A style appropriate for placeholder text.
- [static var link: LinkShapeStyle](./link.md)
  A style appropriate for links.
- [static var fill: FillShapeStyle](./fill.md)
  An overlay fill style for filling shapes.
- [static var windowBackground: WindowBackgroundShapeStyle](./windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/selection)*