# reorderContainer(for:in:isEnabled:move:)

**Framework**: SwiftUI  
**Kind**: method

Defines a container that allows its items to be reordered.

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
func reorderContainer<Item, CollectionID>(for item: Item.Type, in collectionID: CollectionID.Type, isEnabled: Bool = true, move: @escaping (ReorderDifference<Item.ID, CollectionID>) -> ()) -> some View where Item : Identifiable, CollectionID : Hashable, CollectionID : Sendable, Item.ID : Sendable
```

## Mentions

- [Reordering items in lists, stacks, grids, and custom layouts](reordering-items-in-lists-stacks-grids-and-custom-layouts.md)

#### Discussion

Declare this modifier on your container or layout view to make it a reorderable container. Then, apply [`reorderable()`](dynamicviewcontent/reorderable().md) to the content of your container to make those items reorderable.

Use this overload if your container has multiple collections in it. If your container only has a single collection, use the convenience [`reorderContainer(for:isEnabled:move:)`](view/reordercontainer(for:isenabled:move:).md) modifier.

A reorderable item within the container can be lifted using a drag gesture. As that item lifts, a placeholder view will take its place to indicate where the moved view will be when dropped. As your user moves the item through the container, the position of the placeholder will update to be the last item that your user dragged over. When they drop the item, the `move` closure will be called with the change provided.

The change is provided as a difference to the closure. The difference contains the identifiers of the moved items, in the order that the user selected them. It also contains a destination value, which indicates where to insert the item.

This example shows a list of reminders. Items can be moved within the list’s underlying collections.

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

- item: The type of reorderable items in the container.
- collectionID: The type used to identify collections of reorderable items in the container.
- isEnabled: Whether the container allows reordering.
- move: A closure that provides the change at the end of a session.

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
- [func reorderContainer<Item, ItemID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, isEnabled: Bool, move: (ReorderDifference<ItemID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](view/reordercontainer(for:itemid:isenabled:move:).md)
  Defines a container that allows its items to be reordered.
- [func reorderContainer<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:itemid:in:isenabled:move:).md)
  Defines a container that allows its items to be reordered.
- [func reorderDestination<Item, CollectionID>(for: Item.Type, in: CollectionID.Type) -> ReorderDifference<Item.ID, CollectionID>.Destination?](dropsession/reorderdestination(for:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [func reorderDestination<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type) -> ReorderDifference<ItemID, CollectionID>.Destination?](dropsession/reorderdestination(for:itemid:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [struct ReorderDifference](reorderdifference.md)
  The difference produced by a reordering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/reordercontainer(for:in:isenabled:move:))*