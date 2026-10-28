# badge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Generates a badge for the view from an integer value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func badge(_ count: Int) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func badge(_ resource: LocalizedStringResource?) -> some View
```

```swift
nonisolated
func badge(_ key: LocalizedStringKey?) -> some View
```

```swift
nonisolated
func badge(_ label: Text?) -> some View
```

```swift
nonisolated
func badge<S>(_ label: S?) -> some View where S : StringProtocol
```

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

The following example shows a [`List`](../list.md) with the value of `recentItems.count` represented by a badge on one of the rows:

```swift
List {
    Text("Recents")
        .badge(recentItems.count)
    Text("Favorites")
}
```

![A table with two rows, titled Recents and Favorites. The first row](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-badge-1@2x.png)

## Parameters

- `count`: An integer value to display in the badge. Set the value to zero to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/badge(_:)-8adyq)*