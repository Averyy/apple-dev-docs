# listRowBackground(_:)

**Framework**: SwiftUI  
**Kind**: method

Places a custom background view behind a list row item.

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
func listRowBackground<V>(_ view: V?) -> some View where V : View
```

#### Return Value

A list row view with `view` as its background view.

#### Discussion

Use `listRowBackground(_:)` to place a custom background view behind a list row item.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI [`ForEach`](foreach.md) structure computes views for each element of the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. The `listRowBackground(_:)` modifier then places the view you supply behind each of the list row items:

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
                    .listRowBackground(Ellipse()
                                        .background(Color.clear)
                                        .foregroundColor(.purple)
                                        .opacity(0.3)
                    )
            }
        }
    }
}
```

![A screenshot showing the placement of an image as the background to](https://docs-assets.developer.apple.com/published/149e5b46ecc387e7e071f9b4796f462b/SwiftUI-View-listRowBackground%402x.png)

## Parameters

- `view`: The   to use as the background behind the list   row view.

## See Also

- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](view/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [struct AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior.md)
  The styling of views with respect to alternating row backgrounds.
- [var backgroundProminence: BackgroundProminence](environmentvalues/backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.
- [struct BackgroundProminence](backgroundprominence.md)
  The prominence of backgrounds underneath other views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowbackground(_:))*