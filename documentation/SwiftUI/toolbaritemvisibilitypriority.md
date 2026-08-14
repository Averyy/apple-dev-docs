# ToolbarItemVisibilityPriority

**Framework**: SwiftUI  
**Kind**: struct

A value that defines the visibility priority of a toolbar item.

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
struct ToolbarItemVisibilityPriority
```

#### Overview

When a toolbar runs out of space, it moves items into an overflow menu. Visibility priority controls the order in which that happens: items with a lower priority move first, keeping higher-priority items visible longer as the window shrinks.

Use values of this type with the [`visibilityPriority(_:)`](toolbarcontent/visibilitypriority(_:).md) modifier. For example, to keep a share button visible longer than an archive button:

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
- [static let automatic: ToolbarItemVisibilityPriority](toolbaritemvisibilitypriority/automatic.md)
  The default priority that lets the system determine the item’s visibility in the toolbar.
- [static let low: ToolbarItemVisibilityPriority](toolbaritemvisibilitypriority/low.md)
  A priority that moves the item to the overflow menu before items with the default or high priority.
- [static let high: ToolbarItemVisibilityPriority](toolbaritemvisibilitypriority/high.md)
  A priority that keeps the item in the toolbar longer than items with the default or low priority.
### Creating custom priorities
- [init(lowerThan: ToolbarItemVisibilityPriority)](toolbaritemvisibilitypriority/init(lowerthan:).md)
  Creates a priority lower than the specified value.
- [init(higherThan: ToolbarItemVisibilityPriority)](toolbaritemvisibilitypriority/init(higherthan:).md)
  Creates a priority higher than the specified value.

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func visibilityPriority(ToolbarItemVisibilityPriority) -> some ToolbarContent](toolbarcontent/visibilitypriority(_:).md)
  Defines the visibility priority for a toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority)*