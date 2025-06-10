# dragContainer(for:in:selection:_:)

**Framework**: Assignables  
**Kind**: method

A container with single item selection and draggable views. The drag payload is identifiable and is based on the current selection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<Item>(for itemType: Item.Type = Item.self, in namespace: Namespace.ID? = nil, selection: @autoclosure @escaping () -> Item.ID?, _ payload: @escaping (Item.ID) -> Item?) -> some View where Item : Transferable, Item : Identifiable, Item.ID : Sendable
```

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

In an example below, an app presents a view with `Fruit` values.

```None
   @State private var fruits: [Fruit]
   @State private var selection: Fruit.ID?

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               FruitView(fruit)
                   .draggable(containerItemID: fruit.id)
           }
       }
       .dragContainer(selection: selection) { id in
          fruit(id: id)
       }
   }

   /// Returns a Fruit value with given identifier, if present.
   func fruit(id: Fruit.ID) -> Fruit? { ... }

   struct Fruit: Transferable, Identifiable {
       var id: String
       ...
   }
```

## Parameters

- `itemType`: A type of the dragged item.
- `namespace`: An optional namespace that identifies the drag container.
- `selection`: A closure returning the identifier of the   currently selected item.   Return   to indicate that the selection is empty.
- `payload`: A closure that returns the item with   the given identifier. Return   to disable drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/dragcontainer(for:in:selection:_:)-4upk6)*