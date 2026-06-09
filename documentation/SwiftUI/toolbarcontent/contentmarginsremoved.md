# contentMarginsRemoved(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures whether the content margins are removed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func contentMarginsRemoved(_ removed: Bool = true) -> some ToolbarContent
```

#### Discussion

Use this modifier to remove the default padding around a toolbar item’s content. This is useful for content that goes to the edge of the item.

```swift
.toolbar {
    ToolbarItem {
        CustomButton()
    }
    .contentMarginsRemoved()
}
```

## Parameters

- `removed`: Whether the content margins should be removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontent/contentmarginsremoved(_:))*