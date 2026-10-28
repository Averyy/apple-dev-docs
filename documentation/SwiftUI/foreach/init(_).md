# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ data: Data) where ID == Data.Element.ID, Content == TableRow<Data.Element>, Data.Element : Identifiable
```

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to `Hashable`, and `Content` conforms to `TableRowContent`.

## Discussion

The following example creates a `Person` type that conforms to [`Identifiable`](../../Swift/identifiable.md), and an array of this type called `people`. A `ForEach` instance iterates over the array, producing new [`TableRow`](../tablerow.md) instances implicitly.

```swift
private struct Person: Identifiable {
    var id = UUID()
    var name: String
}

@State private var people: [Person] = /* ... */

Table(of: Person.self) {
    TableColumn("ID", value: \.id.uuidString)
    TableColumn("Name", value: \.name)
} rows: {
    Section("Team") {
        /* This is equivalent to the line below:
        ForEach(people) { TableRow($0) }
        */
        ForEach(people)
    }
}
```

## Parameters

- `data`: The identified data that the [`ForEach`](../foreach.md) instance uses to create table rows dynamically.

## See Also

### Creating a collection
- [init(_:content:)](./init%28_,content%29.md)
  Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](./init%28_,id,content%29.md)
  Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init<V>(sections: V, content: (SectionConfiguration) -> Content)](./init%28sections,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init<V>(subviews: V, content: (Subview) -> Content)](./init%28subviews,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:))*