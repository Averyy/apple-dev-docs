# init(_:systemImage:sources:selection:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a picker bound to a collection of bindings that generates its label from a string.

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
init<C, S>(_ title: S, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ViewBuilder content: () -> Content) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>
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
    "Border Thickness",
    sources: $selectedObjectBorders,
    selection: \.thickness
) {
    ForEach(Thickness.allCases) { thickness in
        Text(thickness.rawValue)
    }
}
```

## Parameters

- `title`: A string that describes the purpose of selecting an option.
- `systemImage`: The name of the image resource to lookup.
- `sources`: A collection of values used as the source for displaying   the Picker’s selection.
- `selection`: The key path of the values that determines the   currently-selected options. When a user selects an option from the   picker, the values at the key path of all items in the    collection are updated with the selected option.
- `content`: A view that contains the set of options.

## See Also

- [init(_:image:selection:content:)](picker/init(_:image:selection:content:).md)
  Creates a picker that generates its label from a localized string key and image resource
- [init(_:image:sources:selection:content:)](picker/init(_:image:sources:selection:content:).md)
  Creates a picker bound to a collection of bindings that generates its label from a string and image resource.
- [init(_:systemImage:selection:content:)](picker/init(_:systemimage:selection:content:).md)
  Creates a picker that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:))*