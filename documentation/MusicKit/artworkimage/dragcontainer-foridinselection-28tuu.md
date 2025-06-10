# dragContainer(for:id:in:selection:_:)

**Framework**: MusicKit  
**Kind**: method

A container with single item selection and draggable views. The drag payload is based on the current selection and provided identifiers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<Item, ItemID>(for itemType: Item.Type = Item.self, id: @escaping (Item) -> ItemID, in namespace: Namespace.ID? = nil, selection: @autoclosure @escaping () -> ItemID?, _ payload: @escaping (ItemID) -> Item?) -> some View where Item : Transferable, ItemID : Hashable, ItemID : Sendable
```

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

In an example below, an app presents a view with `Fruit` values. `Fruit` uses the name as its identifier.

```swift
   @State private var fruits: [Fruit]
   @State private var selection: Fruit.ID?

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               FruitView(fruit)
                   .draggable(containerItemID: fruit.name)
           }
       }
       .dragContainer(selection: selection, id: \.name) { draggedID in
          fruit(id: id)
       }
   }

   func fruit(id: String) -> Fruit? { ... }

   struct Fruit: Transferable {
       var name: String
       ...
   }
```

## Parameters

- `itemType`: A type of the dragged item.
- `id`: A closure that returns the identifier of a given dragged item.
- `namespace`: An optional namespace that identifies   the drag container.
- `selection`: A closure returning the item that is currently selected.   Return   to indicate that the selection is empty.
- `payload`: A closure that returns the item with a given identifier.   Return   to disable drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/dragcontainer(for:id:in:selection:_:)-28tuu)*