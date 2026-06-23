# reorderDestination(for:itemID:in:)

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
func reorderDestination<Item, ItemID, CollectionID>(for item: Item.Type, itemID: KeyPath<Item, ItemID>, in collectionID: CollectionID.Type = ReorderableSingleCollectionIdentifier.self) -> ReorderDifference<ItemID, CollectionID>.Destination?
```

#### Discussion

Use the `ItemID` and `CollectionID` types of your [`reorderContainer(for:in:isEnabled:move:)`](view/reordercontainer(for:in:isenabled:move:).md) modifier to look up the destination value.

This value can be `nil`, if the container was unable to determine a placement for the items. This can happen if someone drags items into the destination but does not interact with any of the container items to determine a concrete position. You should still accept these items into the container. This example demostrates appending those values to the end of the collection:

```swift
struct ContentView: View {
    @State var accounts: [Account] = []

    var body: some View {
        VStack {
            ForEach(accounts, id: \.uuid) { account in
                AccountView(account)
            }
            .reorderable()
        }
        .reorderContainer(for: Account.self, itemID: \.uuid) {
            (difference) in
            apply(difference: difference)
        }
        .dragContainer(for: Account.self) { userIDs in
            findAccounts(ids: userIDs)
        }
        .dropDestination(for: Account.self) { items, session in
            if let destinationIndex = session.reorderDestination(
                for: Account.self, itemID: \.uuid)?.index(
                    in: accounts)
            {
                accounts.insert(
                    contentsOf: items, at: destinationIndex)
            } else {
                accounts.append(contentsOf: items)
            }
        }
    }
}
```

## Parameters

- `item`: The type of reorderable items in the container.
- `collectionID`: The identifier type for collections in your container.

## See Also

- [Making a card game with drag, drop, and reordering in SwiftUI](making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md)
  Move cards between positions in a card game using drag, drop, and reordering modifiers.
- [func reorderable() -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable.md)
  Enables reordering of views from this content inside the scope of a reorderable container modifier.
- [func reorderable(collectionID: some Hashable & Sendable) -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable(collectionid:).md)
  Enables reordering views from this content within and between sections in the scope of a reorderable container modifier.
- [struct ReorderableSingleCollectionIdentifier](reorderablesinglecollectionidentifier.md)
  An opaque, empty type used to identify reorderable containers and modifiers with only a single collection.
- [func reorderContainer<Item>(for: Item.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](view/reordercontainer(for:isenabled:move:).md)
  Defines a container of reorderable views.
- [func reorderContainer<Item, CollectionID>(for: Item.Type, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:in:isenabled:move:).md)
  Defines a container of reorderable views, with a type you specify to identify sections.
- [func reorderContainer<Item, ItemID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, isEnabled: Bool, move: (ReorderDifference<ItemID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](view/reordercontainer(for:itemid:isenabled:move:).md)
  Defines a container of reorderable views, with a type and keypath you specify to identify items.
- [func reorderContainer<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:itemid:in:isenabled:move:).md)
  Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections.
- [func reorderDestination<Item, CollectionID>(for: Item.Type, in: CollectionID.Type) -> ReorderDifference<Item.ID, CollectionID>.Destination?](dropsession/reorderdestination(for:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [struct ReorderDifference](reorderdifference.md)
  The difference that a reordering operation produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/reorderdestination(for:itemid:in:))*