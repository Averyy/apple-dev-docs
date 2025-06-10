# dragContainer(for:in:selection:_:)

**Framework**: FamilyControls  
**Kind**: method

A container with multiple selection and draggable views. The drag payload is identifiable and is based on the current selection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainer<Item, Data>(for itemType: Item.Type = Item.self, in namespace: Namespace.ID? = nil, selection: @autoclosure @escaping () -> Array<Item.ID>, _ payload: @escaping (Array<Item.ID>) -> Data) -> some View where Item : Transferable, Item : Identifiable, Item == Data.Element, Data : Collection, Item.ID : Sendable
```

#### Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

In an example below, an app presents a view with `Fruit` values. When a user starts drag, SwiftUI uses the selection to put together the list of item identifiers to drag.

```swift
   var fruits: [Fruit]
   @State var selection: [Fruit.ID]

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               FruitView(fruit)
                   .draggable(containerItemID: fruit.id)
           }
       }
       .dragContainer(selection: selection) { ids in
          fruits(ids: ids)
       }
   }

   /// Returns the Fruit values with given identifiers.
   func fruits(ids: [Fruit.ID]) -> [Fruit] { ... }

   struct Fruit: Transferable, Identifiable { ... }
```

## Parameters

- `itemType`: A type of the dragged items.
- `namespace`: An optional namespace that identifies   the drag container.
- `selection`: Identifiers of the currently selected items.
- `payload`: A closure which is called when   a drag operation begins. As an argument, the closure receives either   the identifiers of all the selected items, if the dragged item is   a part of selection, or only the identifier of the dragged item, if it is   not part of the selection. With the passed identifiers,   put together the payload to drag, and return from the closure.   The number of returned items can be different from the number   of dragged identifiers. Only the views that correspond to returned   item identifiers will be dragged.   Return an empty   to disable the drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/dragcontainer(for:in:selection:_:)-1e0yx)*