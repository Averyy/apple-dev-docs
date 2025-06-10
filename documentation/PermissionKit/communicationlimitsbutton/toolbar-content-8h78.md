# toolbar(content:)

**Framework**: PermissionKit  
**Kind**: method

Populates the toolbar or navigation bar with the specified items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 7.0+

## Declaration

```swift
nonisolated
func toolbar<Content>(@ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
```

#### Discussion

Use this method to populate a toolbar with a collection of views that you provide to a toolbar view builder.

The toolbar modifier expects a collection of toolbar items which you can provide either by supplying a collection of views with each view wrapped in a `ToolbarItem`, or by providing a collection of views as a `ToolbarItemGroup`. The example below uses a collection of `ToolbarItem` views to create a macOS toolbar that supports text editing features:

```None
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

Although it’s not mandatory, wrapping a related group of toolbar items together in a `ToolbarItemGroup` provides a one-to-one mapping between controls and toolbar items which results in the correct layout and spacing on each platform. For design guidance on toolbars, see [`Toolbars`](https://developer.apple.com/design/Human-Interface-Guidelines/toolbars) in the Human Interface Guidelines.

## Parameters

- `content`: The items representing the content of the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/toolbar(content:)-8h78)*