# toolbarItemHidden(_:)

**Framework**: PermissionKit  
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

```None
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

- `hidden`: Whether the view in a control group toolbar item is   hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/toolbaritemhidden(_:))*