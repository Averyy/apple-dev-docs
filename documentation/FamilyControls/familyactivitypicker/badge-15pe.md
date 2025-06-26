# badge(_:)

**Framework**: FamilyControls  
**Kind**: method

Generates a badge for the view from an integer value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func badge(_ count: Int) -> some View
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

The following example shows a `List` with the value of `recentItems.count` represented by a badge on one of the rows:

```swift
List {
    Text("Recents")
        .badge(recentItems.count)
    Text("Favorites")
}
```

## Parameters

- `count`: An integer value to display in the badge.   Set the value to zero to hide the badge.

## See Also

- [func badge(LocalizedStringKey?) -> some View](familyactivitypicker/badge(_:)-15e4b.md)
  Generates a badge for the view from a localized string key.
- [func badge<S>(S?) -> some View](familyactivitypicker/badge(_:)-720cq.md)
  Generates a badge for the view from a string.
- [func badge(Text?) -> some View](familyactivitypicker/badge(_:)-7hd2m.md)
  Generates a badge for the view from a text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/badge(_:)-15pe)*