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
func axisBehavior(_ behavior: ToolbarItemAxisBehavior) -> some CustomizableToolbarContent
```

#### Discussion

Use this modifier to control which bar axes a toolbar item can appear in.

The following example restricts an item to the horizontal axis. The item can only appear in a horizontal bar.

```swift
.toolbar(id: "main") {
    ToolbarItem(id: "enable") {
        Toggle(isOn: $isOn) { ... }
    }
    .axisBehavior(.horizontalOnly)
}
```

If both horizontal & vertical bars are present and the item is `.verticalPreferred`, the system prefers placing the item vertically.

## Parameters

- `behavior`: The axis behavior of the item.

## See Also

- [func customizationBehavior(ToolbarCustomizationBehavior) -> some CustomizableToolbarContent](customizabletoolbarcontent/customizationbehavior(_:).md)
  Configures the customization behavior of customizable toolbar content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/axisbehavior(_:))*