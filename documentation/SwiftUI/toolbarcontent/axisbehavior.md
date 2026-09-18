# axisBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

The bar axis behavior of the toolbar item.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
func axisBehavior(_ behavior: ToolbarItemAxisBehavior) -> some ToolbarContent
```

#### Discussion

Use this modifier to control which bar axes a toolbar item can appear in.

The following example restricts an item to the horizontal axis. The item can only appear in a horizontal bar.

```swift
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        Toggle(isOn: $isOn) { ... }
    }
    .axisBehavior(.horizontalOnly)
}
```

If both horizontal & vertical bars are present and the item is `.verticalPreferred`, the system prefers placing the item in the vertical bar.

## Parameters

- `behavior`: The axis behavior of the item.

## See Also

- [struct ToolbarItemAxisBehavior](toolbaritemaxisbehavior.md)
  Describes the bar axis behavior of a toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontent/axisbehavior(_:))*