# dragContainer(for:in:_:)

**Framework**: SwiftUI  
**Kind**: method

A container with draggable views where the drag payload is based on multiple identifiers of dragged items.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<Item, Data>(for itemType: Item.Type = Item.self, in namespace: Namespace.ID? = nil, _ payload: @escaping (Array<Item.ID>) -> Data) -> some View where Item : Transferable, Item : Identifiable, Item == Data.Element, Data : Collection, Item.ID : Sendable
```

## Mentions

- [Reordering items in lists, stacks, grids, and custom layouts](reordering-items-in-lists-stacks-grids-and-custom-layouts.md)

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Provide the selected identifiers list to SwiftUI using `dragContainerSelection(_:containerNamespace)` modifier. In a case when there’s no selection information available, SwiftUI passes the dragged item identifier to the `payload` closure.

In an example below, an app presents a view with `Fruit` values. When a user starts drag, SwiftUI uses the selection to put together the list of item identifiers to drag.

```swift
   var fruits: [Fruit]
   @State private var selection: [Fruit.ID]

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               FruitView(fruit)
                   .draggable(containerItemID: fruit.id)
           }
       }
       .dragContainer(for: Fruit.self) { ids in
          fruits(with: ids)
       }
       .dragContainerSelection(selection)
   }

   func fruits(with ids: [UUID]) -> [Fruit] { ... }

   struct Fruit: Transferable, Identifiable { ... }
```

To enable multi-item drag, apply this modifier to a container view and mark each draggable child with [`draggable(_:)`](view/draggable(_:).md) or [`draggable(containerItemID:containerNamespace:)`](view/draggable(containeritemid:containernamespace:).md).

## Parameters

- `itemType`: A type of the dragged items.
- `namespace`: A namespace that identifies the drag container.
- `payload`: A closure which is called when a drag operation begins. As an argument, the closure receives either the identifiers of all the selected items, if the dragged item is a part of selection or only the identifier of the dragged item, if it is not part of the selection. With the passed identifiers, put together the payload to drag, and return from the closure. Return an empty `Collection` to disable the drag.

## See Also

- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [struct DragConfiguration](dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:itemID:in:_:)](view/dragcontainer(for:itemid:in:_:).md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](view/dragcontainerselection(_:containernamespace:).md)
  Provides multiple item selection support for drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dragcontainer(for:in:_:))*