# toolbar(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Populates the toolbar or navigation bar with the views you provide.

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
func toolbar<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View
```

**Other overloads**:

```swift
nonisolated
func toolbar<Content>(@ContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
```

## Discussion

Use this modifier to add content to the toolbar. The toolbar modifier expects a collection of toolbar items that you can provide either by supplying a collection of views with each view wrapped in a [`ToolbarItem`](../toolbaritem.md), or by providing a collection of views as a [`ToolbarItemGroup`](../toolbaritemgroup.md). The example below adds views to using a toolbar item group to support text editing features:

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

![A window showing a font size selector, and toggles for bold, italic.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-Styling-ToolbarContent@2x.png)

## Parameters

- `content`: The views representing the content of the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbar(content:)-7vdkx)*