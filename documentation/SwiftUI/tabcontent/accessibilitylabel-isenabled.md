# accessibilityLabel(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Adds a label to the tab that describes its contents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityLabel(_ label: LocalizedStringResource, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

#### Discussion

Use this method to provide an accessibility label for a tab that contains content like an icon. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Library tab” because a tab already has a trait that identifies it as a tab.

```swift
var body: some View {
    TabView {
        Tab {
            FavoritesView()
        } label: {
            Image(systemName: "star.fill")
        }
        .accessibilityLabel("Favorites")
    }
}
```

## Parameters

- `label`: The accessibility label to apply.
- `isEnabled`: If true the accessibility label is applied; otherwise   the accessibility label is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilitylabel(_:isenabled:))*