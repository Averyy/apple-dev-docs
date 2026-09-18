# visibilityPriority(_:)

**Framework**: SwiftUI  
**Kind**: method

Defines the visibility priority for a toolbar item.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 26.1+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func visibilityPriority(_ priority: ToolbarItemVisibilityPriority) -> some CustomizableToolbarContent
```

#### Discussion

When toolbar space is limited, items with a lower priority move into the overflow menu before items with a higher priority. The default is [`automatic`](toolbaritemvisibilitypriority/automatic.md).

In the following example, `PrimaryControl` stays visible in the toolbar longer than `SecondaryControl`:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ToolbarItem {
                    SecondaryControl()
                }
                ToolbarItem {
                    PrimaryControl()
                }
                .visibilityPriority(.high)
            }
    }
}
```

## Parameters

- `priority`: The visibility priority for this toolbar item.

## See Also

- [func hidden(Bool) -> some CustomizableToolbarContent](customizabletoolbarcontent/hidden(_:).md)
  Hides a toolbar item within its toolbar.
- [func sharedBackgroundVisibility(Visibility) -> some CustomizableToolbarContent](customizabletoolbarcontent/sharedbackgroundvisibility(_:).md)
  Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/visibilitypriority(_:))*