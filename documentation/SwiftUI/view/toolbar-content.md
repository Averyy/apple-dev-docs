# toolbar(content:)

**Framework**: SwiftUI  
**Kind**: method

Populates the toolbar or navigation bar with the specified items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func toolbar<Content>(@ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
```

#### Discussion

Use this method to populate a toolbar with a collection of views that you provide to a toolbar view builder.

The toolbar modifier expects a collection of toolbar items which you can provide either by supplying a collection of views with each view wrapped in a [`ToolbarItem`](toolbaritem.md), or by providing a collection of views as a [`ToolbarItemGroup`](toolbaritemgroup.md). The example below uses a collection of [`ToolbarItem`](toolbaritem.md) views to create a macOS toolbar that supports text editing features:

```swift
struct StructToolbarItemGroupView: View {
    @State private var text = ""
    @State private var bold = false
    @State private var italic = false
    @State private var fontSize = 12.0

    var displayFont: Font {
        let font = Font.system(size: CGFloat(fontSize),
                               weight: bold == true ? .bold : .regular)
        return italic == true ? font.italic() : font
    }

    var body: some View {
        TextEditor(text: $text)
            .font(displayFont)
            .toolbar {
                ToolbarItemGroup {
                    Slider(
                        value: $fontSize,
                        in: 8...120,
                        minimumValueLabel:
                            Text("A").font(.system(size: 8)),
                        maximumValueLabel:
                            Text("A").font(.system(size: 16))
                    ) {
                        Text("Font Size (\(Int(fontSize)))")
                    }
                    .frame(width: 150)
                    Toggle(isOn: $bold) {
                        Image(systemName: "bold")
                    }
                    Toggle(isOn: $italic) {
                        Image(systemName: "italic")
                    }
                }
            }
            .navigationTitle("My Note")
    }
}
```

![A window showing a font size selector, and toggles for bold, italic.](https://docs-assets.developer.apple.com/published/b7e3a3c785ffaf50a0cf94db31a14341/SwiftUI-View-Styling-ToolbarContent%402x.png)

Although it’s not mandatory, wrapping a related group of toolbar items together in a [`ToolbarItemGroup`](toolbaritemgroup.md) provides a one-to-one mapping between controls and toolbar items which results in the correct layout and spacing on each platform. For design guidance on toolbars, see [`Toolbars`](https://developer.apple.com/design/Human-Interface-Guidelines/toolbars) in the Human Interface Guidelines.

## Parameters

- `content`: The items representing the content of the toolbar.

## See Also

- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbar(content:))*