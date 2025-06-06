# listRowInsets(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies an inset to the rows in a list.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func listRowInsets(_ insets: EdgeInsets?) -> some View
```

#### Return Value

A view that uses the given edge insets when used as a list cell.

#### Discussion

Use `listRowInsets(_:)` to change the default padding of the content of list items.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI [`ForEach`](foreach.md) structure computes views for each element of the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. The `listRowInsets(_:)` modifier then changes the edge insets of each row of the list according to the [`EdgeInsets`](edgeinsets.md) provided:

```swift
struct ContentView: View {
    enum Flavor: String, CaseIterable, Identifiable {
        var id: String { self.rawValue }
        case vanilla, chocolate, strawberry
    }

    var body: some View {
        List {
            ForEach(Flavor.allCases) {
                Text($0.rawValue)
                    .listRowInsets(.init(top: 0,
                                         leading: 25,
                                         bottom: 0,
                                         trailing: 0))
            }
        }
    }
}
```

![A screenshot showing a list with leading 25 point inset on each row.](https://docs-assets.developer.apple.com/published/0b10922ed606478b5a4155f90ed18221/SwiftUI-View-ListRowInsets%402x.png)

## Parameters

- `insets`: The   to apply to the edges of the   view.

## See Also

- [func listRowHoverEffect(HoverEffect?) -> some View](view/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](view/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
- [func listItemTint(_:)](view/listitemtint(_:).md)
  Sets a fixed tint color for content in a list.
- [struct ListItemTint](listitemtint.md)
  A tint effect configuration that you can apply to content in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of a row in a `List`. The default minimum height of a row in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowinsets(_:))*