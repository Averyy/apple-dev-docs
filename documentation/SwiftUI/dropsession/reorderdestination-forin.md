# reorderDestination(for:in:)

**Framework**: SwiftUI  
**Kind**: method

Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func reorderDestination<Item, CollectionID>(for item: Item.Type, in collectionID: CollectionID.Type = ReorderableSingleCollectionIdentifier.self) -> ReorderDifference<Item.ID, CollectionID>.Destination? where Item : Identifiable
```

## Mentions

- [Reordering items in lists, stacks, grids, and custom layouts](reordering-items-in-lists-stacks-grids-and-custom-layouts.md)

#### Discussion

Use the `ItemID` and `CollectionID` types of your [`reorderContainer(for:in:isEnabled:move:)`](view/reordercontainer(for:in:isenabled:move:).md) modifier to look up the destination value.

This value can be `nil`, if the container was unable to determine a placement for the items. This can happen if the user drags items into the destination but does not interact with any of the container items to determine a concrete position. You should still accept these items into the container. In this example, those values are appended to the end of the collection:

```swift
struct ContentView: View {
    @State var contacts: [Contact] = []

    var body: some View {
        VStack {
            ForEach(contacts) { contact in
                ContactView(contact)
            }
            .reorderable()
        }
        .reorderContainer(for: Contact.ID.self) { difference in
            difference.apply(to: &contacts)
        }
        .dragContainer(for: Contact.self) { itemID in
            contacts.first { $0.id == itemID }.map { [$0] } ?? []
        }
        .dropDestination(for: Contact.self) { items, session in
            if let destinationIndex = session.reorderDestination(
                for: Contact.ID.self)?.index(in: contacts)
            {
                contacts.insert(
                    contentsOf: items, at: destinationIndex)
            } else {
                contacts.append(contentsOf: items)
            }
        }
    }
}
```

- item: The type of reorderable items in the container.
- collectionID: The identifier type for collections in your container.

## See Also

- [Making a card game with drag, drop, and reordering in SwiftUI](making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md)
  Move cards between positions in a card game using drag, drop, and reordering modifiers.
- [func reorderable() -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable.md)
  Enables the views of this content to be reordered when used within the scope of a [`reorderContainer(for:in:isEnabled:move:)`](view/reordercontainer(for:in:isenabled:move:).md) modifier.
- [func reorderable(collectionID: some Hashable & Sendable) -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable(collectionid:).md)
  Enables the views of this content to be reordered when used within the scope of a [`reorderContainer(for:in:isEnabled:move:)`](view/reordercontainer(for:in:isenabled:move:).md) modifier.
- [struct ReorderableSingleCollectionIdentifier](reorderablesinglecollectionidentifier.md)
  An opaque, empty type used to identify reorderable containers and modifiers expecting only a single collection.
- [func reorderContainer<Item>(for: Item.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](view/reordercontainer(for:isenabled:move:).md)
  Defines a container that allows its items to be reordered.
- [func reorderContainer<Item, CollectionID>(for: Item.Type, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:in:isenabled:move:).md)
  Defines a container that allows its items to be reordered.
- [func reorderContainer<Item, ItemID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, isEnabled: Bool, move: (ReorderDifference<ItemID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](view/reordercontainer(for:itemid:isenabled:move:).md)
  Defines a container that allows its items to be reordered.
- [func reorderContainer<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:itemid:in:isenabled:move:).md)
  Defines a container that allows its items to be reordered.
- [func reorderDestination<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type) -> ReorderDifference<ItemID, CollectionID>.Destination?](dropsession/reorderdestination(for:itemid:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [struct ReorderDifference](reorderdifference.md)
  The difference produced by a reordering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/reorderdestination(for:in:))*