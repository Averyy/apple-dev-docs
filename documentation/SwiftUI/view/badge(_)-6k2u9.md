# badge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Generates a badge for the view from a text view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func badge(_ label: Text?) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func badge(_ resource: LocalizedStringResource?) -> some View
```

```swift
nonisolated
func badge(_ count: Int) -> some View
```

```swift
nonisolated
func badge(_ key: LocalizedStringKey?) -> some View
```

```swift
nonisolated
func badge<S>(_ label: S?) -> some View where S : StringProtocol
```

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

Use this initializer when you want to style a [`Text`](../text.md) view for use as a badge. The following example customizes the badge with the [`monospacedDigit()`](../text/monospaceddigit%28%29.md), [`foregroundColor(_:)`](../text/foregroundcolor%28_%29.md), and [`bold()`](../text/bold%28%29.md) modifiers.

```swift
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

![A table with two rows, titled Recents and Favorites. The first row](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-badge-2@2x.png)

Styling the text view has no effect when the badge appears in a [`TabView`](../tabview.md).

## Parameters

- `label`: An optional [`Text`](../text.md) view to display as a badge. Set the value to `nil` to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/badge(_:)-6k2u9)*