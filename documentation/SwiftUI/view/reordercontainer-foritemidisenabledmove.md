# reorderContainer(for:itemID:isEnabled:move:)

**Framework**: SwiftUI  
**Kind**: method

Defines a container of reorderable views, with a type and keypath you specify to identify items.

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

Declare this modifier on your list, stack, grid, or custom layout to define a reorderable container. Then, apply [`reorderable()`](dynamicviewcontent/reorderable().md) to the content of your container to make those views reorderable.

Use this overload if your container only has one collection within it. If you have multiple collections of reorderable views and you need to provide the type and keypath you use to identify items, use [`reorderContainer(for:itemID:in:isEnabled:move:)`](view/reordercontainer(for:itemid:in:isenabled:move:).md) instead and provide a type for collection identifiers.

A person can lift a reorderable view within the container using a drag gesture. As they lift the item, the system puts a placeholder view in its place to indicate where the view can drop. As they move the item through the container, the position of the placeholder updates to reflect which view the person drags over. When they drop the view, the system calls the `move` closure and provides the change.

The system provides the change as a different to the closure. The difference contains the identifiers of items to move, in the order that the person selected them. It also contains a destination value, which indicates where to insert the item or items.

The following example shows a list of landmark views that a person can move to reorder inside the [`List`](list.md):

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
            apply(difference: difference)
        }
    }
}
```

## Parameters

- `item`: The type of reorderable items in the container.
- `itemID`: A keypath to the identifier used to represent this item.
- `isEnabled`: Whether the container allows reordering.
- `move`: A closure that provides the change at the end of a session.

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
- [func reorderContainer<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View](view/reordercontainer(for:itemid:in:isenabled:move:).md)
  Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections.
- [func reorderDestination<Item, CollectionID>(for: Item.Type, in: CollectionID.Type) -> ReorderDifference<Item.ID, CollectionID>.Destination?](dropsession/reorderdestination(for:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [func reorderDestination<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type) -> ReorderDifference<ItemID, CollectionID>.Destination?](dropsession/reorderdestination(for:itemid:in:).md)
  Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.
- [struct ReorderDifference](reorderdifference.md)
  The difference that a reordering operation produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/reordercontainer(for:itemid:isenabled:move:))*