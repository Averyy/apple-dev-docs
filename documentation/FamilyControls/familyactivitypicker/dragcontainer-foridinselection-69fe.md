# dragContainer(for:id:in:selection:_:)

**Framework**: FamilyControls  
**Kind**: method

A container with multiple selection and draggable views. The drag payload is based on the current selection and provided identifiers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<ItemID, Item, Data>(for itemType: Item.Type = Item.self, id: @escaping (consuming Item) -> ItemID, in namespace: Namespace.ID? = nil, selection: @autoclosure @escaping () -> Array<ItemID>, _ payload: @escaping (Array<ItemID>) -> Data) -> some View where ItemID : Hashable, ItemID : Sendable, Item : Transferable, Item == Data.Element, Data : Collection
```

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

In an example below, an app presents a view with different fruits. `Fruit` does not conform to `Identifiable` but uses its name as identifier.

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
       .dragContainer(selection: selection, id: \.name) { ids in
          fruits(ids: ids)
       }
   }

   /// Returns `Fruit` values with given identifiers.
   func fruits(ids: [String]) -> [Fruit] { ... }

   struct Fruit: Transferable {
       var name: String
       ...
   }
```

## Parameters

- `itemType`: A type of the dragged items.
- `id`: A closure that provides an item’s identifier.
- `namespace`: An optional namespace that identifies   the drag container.
- `selection`: Identifiers of the currently selected items.
- `payload`: A closure which is called when   a drag operation begins. As an argument, the closure receives either the identifiers   of all the selected items, if the dragged item is a part of selection   or only the identifier of the dragged item, if it is   not part of the selection. Using the passed identifiers, put together   the payload to drag, and return from the closure.   The number of returned items can be different from the number   of dragged identifiers. Only the views that correspond to returned   item identifiers will be dragged.   Return an empty   to disable the drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/dragcontainer(for:id:in:selection:_:)-69fe)*