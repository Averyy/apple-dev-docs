# toolbarContainerBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Whether the container this modifier is applied to acts as a toolbar container, reading the toolbar content of its child views and placing that content into its own bar.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func toolbarContainerBehavior(_ behavior: ToolbarContainerBehavior) -> some View
```

## Discussion

By default, a container like a navigation stack may allow toolbar content to flow up to a parent container that can integrate toolbar content from all of its child views, like a navigation split view. Use this modifier to make the container read the toolbar content and draw the toolbar in its container, so that its toolbar always renders as a distinct bar:

```swift
NavigationSplitView {
    SidebarView()
} detail: {
    VStack {
        NavigationStack {
            TopView()
                .toolbar {
                    ToolbarItem(placement: .bottomBar) {
                        Button(
                            "Undo",
                            systemImage: "arrow.uturn.backward"
                        ) { }
                    }
                }
        }
        .toolbarContainerBehavior(.local)

        NavigationStack {
            BottomView()
                .toolbar {
                    ToolbarItem(placement: .bottomBar) {
                        Button(
                            "Favorite",
                            systemImage: "heart.fill"
                        ) { }
                    }
                }
        }
        .toolbarContainerBehavior(.local)
    }
}
```

When applied to a navigation split view, the behavior applies to each column’s explicit or implicit stack.

## Parameters

- `behavior`: The toolbar container behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarcontainerbehavior(_:))*