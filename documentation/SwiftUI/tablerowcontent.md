# TableRowContent

**Framework**: SwiftUI  
**Kind**: protocol

A type used to represent table rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol TableRowContent<TableRowValue>
```

#### Overview

Like with the [`View`](view.md) protocol, you can create custom table row content by declaring a type that conforms to the `TableRowContent` protocol and implementing the required [`tableRowBody`](tablerowcontent/tablerowbody-swift.property.md) property.

```swift
struct GroupOfPeopleRows: TableRowContent {
    @Binding var people: [Person]

    var tableRowBody: some TableRowContent<Person> {
        ForEach(people) { person in
            TableRow(person)
                .itemProvider { person.itemProvider }
        }
        .dropDestination(for: Person.self) { destination, newPeople in
            people.insert(contentsOf: newPeople, at: destination)
        }
    }
}
```

This example uses an opaque result type and specifies that the primary associated type `TableRowValue` for the `tableRowBody` property is a `Person`. From this, SwiftUI can infer `TableRowValue` for the `GroupOfPeopleRows` structure is also `Person`.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting the row body
- [var tableRowBody: Self.TableRowBody](tablerowcontent/tablerowbody-swift.property.md)
  The composition of content that comprise the table row content.
- [associatedtype TableRowBody : TableRowContent](tablerowcontent/tablerowbody-swift.associatedtype.md)
  The type of content representing the body of this table row content.
### Defining the row value
- [associatedtype TableRowValue : Identifiable = Self.TableRowBody.TableRowValue](tablerowcontent/tablerowvalue.md)
  The type of value represented by this table row content.
### Managing interaction
- [func draggable<T>(@autoclosure () -> T) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/draggable(_:).md)
  Activates this row as the source of a drag and drop operation.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/dropdestination(for:action:).md)
  Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onHover(perform: (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/onhover(perform:).md)
  Adds an action to perform when the pointer moves onto or away from the entire row.
- [func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>](tablerowcontent/itemprovider(_:).md)
  Provides a closure that vends the drag representation for a particular data element.
- [struct ItemProviderTableRowModifier](itemprovidertablerowmodifier.md)
  A table row modifier that associates an item provider with some base row content.
### Adding a context menu to a row
- [func contextMenu<M>(menuItems: () -> M) -> ModifiedContent<Self, _ContextMenuTableRowModifier<M>>](tablerowcontent/contextmenu(menuitems:).md)
  Adds a context menu to a table row.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> ModifiedContent<Self, _ContextMenuPreviewTableRowModifier<M, P>>](tablerowcontent/contextmenu(menuitems:preview:).md)
  Adds a context menu with a preview to a table row.
### Instance Methods
- [func selectionDisabled(Bool) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this row.

## Relationships

### Inherited By
- [DynamicTableRowContent](dynamictablerowcontent.md)
### Conforming Types
- [DisclosureTableRow](disclosuretablerow.md)
- [EmptyTableRowContent](emptytablerowcontent.md)
- [ForEach](foreach.md)
- [Group](group.md)
- [ModifiedContent](modifiedcontent.md)
- [OutlineGroup](outlinegroup.md)
- [Section](section.md)
- [TableForEachContent](tableforeachcontent.md)
- [TableHeaderRowContent](tableheaderrowcontent.md)
- [TableOutlineGroupContent](tableoutlinegroupcontent.md)
- [TableRow](tablerow.md)
- [TupleTableRowContent](tupletablerowcontent.md)

## See Also

- [struct TableRow](tablerow.md)
  A row that represents a data value in a table.
- [struct TableHeaderRowContent](tableheaderrowcontent.md)
  A table row that displays a single view instead of columned content.
- [struct TupleTableRowContent](tupletablerowcontent.md)
  A type of table column content that creates table rows created from a Swift tuple of table rows.
- [struct TableForEachContent](tableforeachcontent.md)
  A type of table row content that creates table rows created by iterating over a collection.
- [struct EmptyTableRowContent](emptytablerowcontent.md)
  A table row content that doesn’t produce any rows.
- [protocol DynamicTableRowContent](dynamictablerowcontent.md)
  A type of table row content that generates table rows from an underlying collection of data.
- [struct TableRowBuilder](tablerowbuilder.md)
  A result builder that creates table row content from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowcontent)*