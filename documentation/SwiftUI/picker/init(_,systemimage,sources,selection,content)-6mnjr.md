# init(_:systemImage:sources:selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that generates its label from a localized string resource.

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
@export(implementation)
nonisolated init<C>(_ titleResource: LocalizedStringResource, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>
```

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<C, S>(_ title: S, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>
```

```swift
@export(implementation)
nonisolated init<C>(_ titleKey: LocalizedStringKey, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>
```

## Discussion

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

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `systemImage`: The name of the image resource to lookup.
- `sources`: A collection of values used as the source for displaying the Picker’s selection.
- `selection`: The key path of the values that determines the currently-selected options. When a user selects an option from the picker, the values at the key path of all items in the `sources` collection are updated with the selected option.
- `content`: A view that contains the set of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:)-6mnjr)*