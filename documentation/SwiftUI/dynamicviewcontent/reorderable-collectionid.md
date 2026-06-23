# reorderable(collectionID:)

**Framework**: SwiftUI  
**Kind**: method

Enables reordering views from this content within and between sections in the scope of a reorderable container modifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func reorderable(collectionID: some Hashable & Sendable) -> some DynamicViewContent<Self.Data>
```

## Mentions

- [Reordering items in lists, stacks, grids, and custom layouts](reordering-items-in-lists-stacks-grids-and-custom-layouts.md)

#### Discussion

Declare this modifier on [`DynamicViewContent`](dynamicviewcontent.md) within a reorderable container to allow people to reorder the items in the content using a system drag gesture. A reorderable container is a list, stack, grid, or custom layout that you define with the [`reorderContainer(for:in:isEnabled:move:)`](view/reordercontainer(for:in:isenabled:move:).md) modifier.

Use this modifier when you have multiple collections in the container. Provide a collection identifier to uniquely identify the collection. If your container has a single collection, provide [`ReorderableSingleCollectionIdentifier`](reorderablesinglecollectionidentifier.md) as the identifier, or use [`reorderable()`](dynamicviewcontent/reorderable().md) instead.

This example shows a sectioned list of reminders:

```swift
struct ContentView: View {
    @State private var model = ReminderModel()

    var body: some View {
        List {
            ForEach(model.sections) { section in
                Section(section.name) {
                    ForEach(section.reminders) { reminder in
                        ReminderView(reminder)
                    }
                    .reorderable(collectionID: section.id)
                }
            }
        }
        .reorderContainer(
            for: Reminder.self, in: ReminderModel.Section.ID.self
        ) { difference in
            model.apply(difference: difference)
        }
    }
}
```

## Parameters

- `collectionID`: The identifier that represents this collection. Its value is used in the destination value when reordering.

## See Also

- [Making a card game with drag, drop, and reordering in SwiftUI](making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md)
  Move cards between positions in a card game using drag, drop, and reordering modifiers.
- [func reorderable() -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable.md)
  Enables reordering of views from this content inside the scope of a reorderable container modifier.
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
- [func reorderDestination<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type) -> ReorderDifference<ItemID, CollectionID>.Destination?](dropsession/reorderdestination(for:itemid:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [struct ReorderDifference](reorderdifference.md)
  The difference that a reordering operation produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent/reorderable(collectionid:))*