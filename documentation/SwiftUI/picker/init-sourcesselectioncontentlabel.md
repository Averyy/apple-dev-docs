# init(sources:selection:content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a picker that displays a custom label.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<C>(sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label) where C : RandomAccessCollection
```

#### Discussion

If the wrapped values of the collection passed to `sources` are not all the same, some styles render the selection in a mixed state. The specific presentation depends on the style.  For example, a Picker with a menu style uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the thickness of borders for the currently-selected shapes, which can be of any number.

```swift
enum Thickness: String, CaseIterable, Identifiable {
    case thin
    case regular
    case thick

    var id: String { rawValue }
}

struct Border {
    var color: Color
    var thickness: Thickness
}

@State private var selectedObjectBorders = [
    Border(color: .black, thickness: .thin),
    Border(color: .red, thickness: .thick)
]

Picker(
    sources: $selectedObjectBorders,
    selection: \.thickness
) {
    ForEach(Thickness.allCases) { thickness in
        Text(thickness.rawValue)
    }
} label: {
    Text("Border Thickness")
}
```

## Parameters

- `sources`: A collection of values used as the source for displaying   the Picker’s selection.
- `selection`: The key path of the values that determines the   currently-selected options. When a user selects an option from the   picker, the values at the key path of all items in the    collection are updated with the selected option.
- `content`: A view that contains the set of options.
- `label`: A view that describes the purpose of selecting an option.

## See Also

- [init(_:sources:selection:content:)](picker/init(_:sources:selection:content:).md)
  Creates a picker bound to a collection of bindings that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(sources:selection:content:label:))*