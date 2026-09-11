# contentMarginsRemoved(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures whether the content margins are removed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
func contentMarginsRemoved(_ removed: Bool = true) -> some CustomizableToolbarContent
```

#### Discussion

Use this modifier to remove the default padding around a toolbar item’s content. This is useful for content that goes to the edge of the item.

```swift
.toolbar(id: "main") {
    ToolbarItem(id: "custom") {
        CustomButton()
    }
    .contentMarginsRemoved()
}
```

## Parameters

- `removed`: Whether the content margins should be removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/contentmarginsremoved(_:))*