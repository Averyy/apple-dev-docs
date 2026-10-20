# ToolbarItemVisibilityPriority

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A value that defines the visibility priority of a toolbar item.

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
struct ToolbarItemVisibilityPriority
```

#### Overview

When a toolbar runs out of space, it moves items into an overflow menu. Visibility priority controls the order in which that happens: items with a lower priority move first, keeping higher-priority items visible longer as the window shrinks.

Use values of this type with the [`visibilityPriority(_:)`](./toolbarcontent/visibilitypriority%28_%29.md) modifier. For example, to keep a share button visible longer than an archive button:

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

## Topics

### Getting system priorities
- [static let automatic: ToolbarItemVisibilityPriority](./toolbaritemvisibilitypriority/automatic.md)
  The default priority that lets the system determine the item’s visibility in the toolbar.
- [static let low: ToolbarItemVisibilityPriority](./toolbaritemvisibilitypriority/low.md)
  A priority that moves the item to the overflow menu before items with the default or high priority.
- [static let high: ToolbarItemVisibilityPriority](./toolbaritemvisibilitypriority/high.md)
  A priority that keeps the item in the toolbar longer than items with the default or low priority.
### Creating custom priorities
- [init(lowerThan: ToolbarItemVisibilityPriority)](./toolbaritemvisibilitypriority/init%28lowerthan%29.md)
  Creates a priority lower than the specified value.
- [init(higherThan: ToolbarItemVisibilityPriority)](./toolbaritemvisibilitypriority/init%28higherthan%29.md)
  Creates a priority higher than the specified value.

## Relationships

### Conforms To
- [Comparable](../Swift/comparable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling item visibility
- [func visibilityPriority(ToolbarItemVisibilityPriority) -> some ToolbarContent](./toolbarcontent/visibilitypriority%28_%29.md)
  Defines the visibility priority for a toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority)*