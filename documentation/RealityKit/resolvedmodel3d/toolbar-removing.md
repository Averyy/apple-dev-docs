# toolbar(removing:)

**Framework**: RealityKit  
**Kind**: method

Remove a toolbar item present by default

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func toolbar(removing defaultItemKind: ToolbarDefaultItemKind?) -> some View
```

#### Discussion

Use this modifier to remove toolbar items other `View`s add by default. For example, to remove the sidebar toggle toolbar item provided by `NavigationSplitView`:

```None
NavigationSplitView {
    SidebarView()
        .toolbar(removing: .sidebarToggle)
} detail: {
    DetailView()
}
```

## Parameters

- `defaultItemKind`: The kind of default item to remove


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/toolbar(removing:))*