# visibilityPriority(_:)

**Framework**: SwiftUI  
**Kind**: method

Defines the visibility priority for a toolbar item.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.1+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func visibilityPriority(_ priority: ToolbarItemVisibilityPriority) -> some ToolbarContent
```

#### Discussion

When toolbar space is limited, items with a lower priority move into the overflow menu before items with a higher priority. The default is [`automatic`](toolbaritemvisibilitypriority/automatic.md).

For example, an important control can appear at the trailing edge of the toolbar, but still be shown as the window is made smaller:

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

- [struct ToolbarItemVisibilityPriority](toolbaritemvisibilitypriority.md)
  A value that defines the visibility priority of a toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontent/visibilitypriority(_:))*