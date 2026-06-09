# toolbarItemHidden(_:)

**Framework**: SwiftUI  
**Kind**: method

Hides an individual view within a control group toolbar item.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func toolbarItemHidden(_ hidden: Bool = true) -> some View
```

#### Discussion

Use this modifier to hide individual views of a `ControlGroup` without hiding the entire group. On macOS and iOS, hidden items will be displayed during user customization.

The following example displays a collaboration button in a group when there is an active collaboration session.

```swift
struct ContentView {
    @State private var inCollaboration = false

    var body: some View {
        BrowserView()
            .toolbar(id: "browserToolbar") {
                ToolbarItem(id: "share") {
                    ControlGroup {
                        ShareButton()
                        CollaborationButton()
                            .toolbarItemHidden(!inCollaboration)
                    }
                }
            }
    }
}
```

## Parameters

- `hidden`: Whether the view in a control group toolbar item is hidden.

## See Also

- [func toolbar<Content>(id: String, content: () -> Content) -> some View](view/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [protocol CustomizableToolbarContent](customizabletoolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [struct ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md)
  The customization behavior of customizable toolbar content.
- [struct ToolbarCustomizationOptions](toolbarcustomizationoptions.md)
  Options that influence the default customization behavior of customizable toolbar content.
- [struct SearchToolbarBehavior](searchtoolbarbehavior.md)
  The behavior of a search field in a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbaritemhidden(_:))*