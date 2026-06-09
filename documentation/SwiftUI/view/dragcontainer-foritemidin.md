# dragContainer(for:itemID:in:_:)

**Framework**: SwiftUI  
**Kind**: method

A container with draggable views.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<ItemID, Item, Data>(for itemType: Item.Type = Item.self, itemID: KeyPath<Item, ItemID>, in namespace: Namespace.ID? = nil, _ payload: @escaping (Array<ItemID>) -> Data) -> some View where ItemID : Hashable, ItemID : Sendable, Item : Transferable, Item == Data.Element, Data : Collection
```

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

In an example below, an app presents a view with `Fruit` values. `Fruit` does not conform to `Identifiable` but uses its name as its identifier.

```swift
   @State private var fruits: [Fruit]
   @State private var selection: [String]

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               FruitView(fruit)
                   .draggable(containerItemID: fruit.name)
           }
       }
       .dragContainer(itemID: \Fruit.name) { ids in
          fruits(with: ids)
       }
   }

   func fruits(with ids: [String]) -> [Fruit] { ... }

   struct Fruit: Transferable {
       var name: String
       ...
   }
```

To enable multi-item drag, apply this modifier to a container view and mark each draggable child with [`draggable(_:)`](view/draggable(_:).md) or [`draggable(containerItemID:containerNamespace:)`](view/draggable(containeritemid:containernamespace:).md).

## Parameters

- `itemType`: A type of the dragged items.
- `itemID`: A closure that provides an item’s identifier.
- `namespace`: A namespace that identifies the drag container.
- `payload`: A closure which is called when a drag operation begins. As an argument, the closure receives either the identifiers of all the selected items, if the dragged item is a part of selection or only the identifier of the dragged item, if it is not part of the selection. Using the passed identifiers, put together the payload to drag, and return from the closure. Return an empty `Collection` to disable the drag.

## See Also

- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [struct DragConfiguration](dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:in:_:)](view/dragcontainer(for:in:_:).md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](view/dragcontainerselection(_:containernamespace:).md)
  Provides multiple item selection support for drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dragcontainer(for:itemid:in:_:))*