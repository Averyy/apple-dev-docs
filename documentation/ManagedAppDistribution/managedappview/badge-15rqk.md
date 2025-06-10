# badge(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Generates a badge for the view from a text view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func badge(_ label: Text?) -> some View
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

Use this initializer when you want to style a `Text` view for use as a badge. The following example customizes the badge with the `Text/monospacedDigit()`, `Text/foregroundColor(_:)`, and `Text/bold()` modifiers.

```None
var body: some View {
    let badgeView = Text("\(recentItems.count)")
        .monospacedDigit()
        .foregroundColor(.red)
        .bold()

    List {
        Text("Recents")
            .badge(badgeView)
        Text("Favorites")
    }
}
```

Styling the text view has no effect when the badge appears in a `TabView`.

## Parameters

- `label`: An optional   view to display as a badge.   Set the value to   to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/badge(_:)-15rqk)*