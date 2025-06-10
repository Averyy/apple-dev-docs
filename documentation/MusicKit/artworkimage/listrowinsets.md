# listRowInsets(_:_:)

**Framework**: MusicKit  
**Kind**: method

Sets the insets of rows in a list on the specified edges.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func listRowInsets(_ edges: Edge.Set = .all, _ length: CGFloat?) -> some View
```

#### Return Value

A view in which the margins of list sections are set to the specified amount

#### Discussion

Use this modifier to change the default insets of list rows on the specified edges.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI `ForEach` structure computes views for each element of the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. The `listRowInsets(_:_:)` modifier then changes the leading inset of each row of the list and leaves the default insets on the other edges untouched:

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
                    .listRowInsets(.leading, 25)
            }
        }
    }
}
```

When applying multiple `listRowInsets` modifiers, modifiers with the same edges will override modifiers higher up in the view hierarchy.

## Parameters

- `edges`: The edges to set the insets to.
- `length`: An amount, given in points, to set the insets to on   the specified edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/listrowinsets(_:_:))*