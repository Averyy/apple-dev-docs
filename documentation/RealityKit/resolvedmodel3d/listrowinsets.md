# listRowInsets(_:)

**Framework**: RealityKit  
**Kind**: method

Applies an inset to the rows in a list.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
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

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI `ForEach` structure computes views for each element of the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. The `listRowInsets(_:)` modifier then changes the edge insets of each row of the list according to the `EdgeInsets` provided:

```None
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

## Parameters

- `insets`: The   to apply to the edges of the   view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/listrowinsets(_:))*