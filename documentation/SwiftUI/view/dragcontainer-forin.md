# dragContainer(for:in:_:)

**Framework**: SwiftUI  
**Kind**: method

A container with draggable views where the drag payload is based on multiple identifiers of dragged items.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func dragContainer<Item, Data>(for itemType: Item.Type = Item.self, in namespace: Namespace.ID? = nil, _ payload: @escaping (Array<Item.ID>) -> Data) -> some View where Item : Transferable, Item : Identifiable, Item == Data.Element, Data : Collection, Item.ID : Sendable
```

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

## Parameters

- `itemType`: A type of the dragged items.
- `namespace`: A namespace that identifies the drag container.
- `payload`: A closure which is called when   a drag operation begins. As an argument, the closure receives either the identifiers   of all the selected items, if the dragged item is a part of selection   or only the identifier of the dragged item, if it is   not part of the selection. With the passed identifiers, put together the payload to drag,   and return from the closure.   Return an empty   to disable the drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dragcontainer(for:in:_:))*