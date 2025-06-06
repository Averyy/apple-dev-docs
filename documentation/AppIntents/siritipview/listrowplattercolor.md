# listRowPlatterColor(_:)

**Framework**: App Intents  
**Kind**: method

Sets the color that the system applies to the row background when this view is placed in a list.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
func listRowPlatterColor(_ color: Color?) -> some View
```

#### Return Value

A view with the specified `color` applied to the system cell.

#### Discussion

Use `View/listRowPlatterColor(_:)` to set the underlying row background color in a list.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI `List` builder iterates over the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. After the list builder finishes, the `listRowPlatterColor(_:)` modifier sets the underlying row background color to the `Color` you specify.

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
                    .listRowPlatterColor(.green)
            }
        }
    }
}
```

## Parameters

- `color`: The   to apply to the system cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/listrowplattercolor(_:))*