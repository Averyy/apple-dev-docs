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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/visibilitypriority(_:))*