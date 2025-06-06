# accessibilityShowsLargeContentViewer(_:)

**Framework**: RealityKit  
**Kind**: method

Adds a custom large content view to be shown by the large content viewer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityShowsLargeContentViewer<V>(@ViewBuilder _ largeContentView: () -> V) -> some View where V : View
```

#### Discussion

Rely on the large content viewer only in situations where items must remain small due to unavoidable design constraints. For example, buttons in a tab bar remain small to leave more room for the main app content.

The following example shows how to add a custom large content view:

```None
var body: some View {
    Button(action: newMessage) {
        Image(systemName: "plus")
    }
    .accessibilityShowsLargeContentViewer {
        Label("New Message", systemImage: "plus")
    }
}
```

Don’t use the large content viewer as a replacement for proper Dynamic Type support. For example, Dynamic Type allows items in a list to grow or shrink vertically to accommodate the user’s preferred font size. Rely on the large content viewer only in situations where items must remain small due to unavoidable design constraints.

For example, views that have their Dynamic Type size constrained with `View/dynamicTypeSize(_:)` may require a large content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/accessibilityshowslargecontentviewer(_:))*