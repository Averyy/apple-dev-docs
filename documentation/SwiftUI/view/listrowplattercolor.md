# listRowPlatterColor(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the color that the system applies to the row background when this view is placed in a list.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
func listRowPlatterColor(_ color: Color?) -> some View
```

#### Return Value

A view with the specified `color` applied to the system cell.

#### Discussion

Use `listRowPlatterColor(_:)` to set the underlying row background color in a list.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI [`List`](list.md) builder iterates over the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. After the list builder finishes, the `listRowPlatterColor(_:)` modifier sets the underlying row background color to the [`Color`](color.md) you specify.

```swift
struct ContentView: View {
    enum Flavor: String, CaseIterable, Identifiable {
        var id: String { self.rawValue }
        case vanilla, chocolate, strawberry
    }

    var body: some View {
        List {
            ForEach(Flavor.allCases) {
                Text($0.rawValue)
                    .listRowPlatterColor(.green)
            }
        }
    }
}
```

## Parameters

- `color`: The   to apply to the system cell.

## See Also

- [func colorScheme(ColorScheme) -> some View](view/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func background<Background>(Background, alignment: Alignment) -> some View](view/background(_:alignment:).md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](view/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](view/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](view/complicationforeground.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowplattercolor(_:))*