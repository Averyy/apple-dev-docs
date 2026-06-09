# reorderContainer(for:itemID:isEnabled:move:)

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
func reorderContainer<Item, ItemID>(for item: Item.Type, itemID: KeyPath<Item, ItemID>, isEnabled: Bool = true, move: @escaping (ReorderDifference<ItemID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View where ItemID : Hashable, ItemID : Sendable
```

#### Discussion

Declare this modifier on your container or layout view to make it a reorderable container. Then, apply [`reorderable(collectionID:)`](dynamicviewcontent/reorderable(collectionid:).md) to the content of your container to make those items reorderable.

Use this overload if your container only has one collection within it. If you have multiple collections of reorderable items, use [`reorderContainer(for:in:isEnabled:move:)`](view/reordercontainer(for:in:isenabled:move:).md) and provide a type for collection identifiers.

A reorderable item within the container can be lifted using a drag gesture. As that item lifts, a placeholder view will take its place to indicate where the moved view will be when dropped. As your user moves the item through the container, the position of the placeholder will update to be the last item that your user dragged over. When they drop the item, the `move` closure will be called with the change provided.

The change is provided as a difference to the closure. The difference contains the identifiers of the moved items, in the order that the user selected them. It also contains a destination value, which indicates where to insert the item.

If your single collection conforms to `MutableCollection`, you can use the difference’s `ReorderDifference/apply(to:)` method to apply the change directly to your closure.

This example shows a stack of landmarks. Items can be moved within the view’s underlying collection.

```swift
struct ContentView: View {
    @State private var landmarks: [Landmark] = []
    @State private var selection = Set<Landmark.ID>()

    var body: some View {
        List(selection: $selection) {
            ForEach(landmarks, id: \.location) { landmark in
                LandmarkView(landmark)
            }
            .reorderable()
        }
        .reorderContainer(for: Landmark.self, id: \.location) {
            (difference) in
            difference.apply(to: &landmarks)
        }
    }
}
```

- item: The type of reorderable items in the container.
- itemID: A keypath to the identifier used to represent this item.
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
- [func reorderContainer<Item, CollectionID>(for: Item.Type, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:in:isenabled:move:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/reordercontainer(for:itemid:isenabled:move:))*