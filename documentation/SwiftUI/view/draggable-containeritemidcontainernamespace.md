# draggable(containerItemID:containerNamespace:)

**Framework**: SwiftUI  
**Kind**: method

Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID? = nil) -> some View where ItemID : Hashable, ItemID : Sendable
```

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

This modifier marks the view as a draggable element of an enclosing `dragContainer(_:containerNamespace:_:)`. Since this modifier does not require to provide the payload, only its identifier, it works lazily (the framework asks to provide the actual dragged items only when drag starts; also, the framework doesn’t have to render a view in order to access its payload).

Applying the `draggable(containerItemID:containerNamespace:)` modifier to a view inside a drag container adds the appropriate gestures for drag and drop to this view. SwiftUI generates a default drag preview for drag.

Below, each `FruitView` is assigned an identifier: a code of a fruit it represents. When dragging begins, the `dragContainer` closure is called with the codes of the selected fruit, or, if a user drags a view that is not selected, the closure receives the identifier of that view as a parameter.

```swift
   var fruits: [Fruit]
   var selectedFruitCodes: [UUID]

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               .draggable(containerItemID: fruit.code)
       }
       .dragContainer { codes in
           fruits(with: codes)
       }
       .dragContainerSelection(selectedFruitCodes)
   }

   func fruits(with codes: [UUID]) -> [Fruit] { ... }

   struct Fruit: Transferable {
       var code: UUID
       ...
   }
```

## Parameters

- `containerItemID`: An identifier of the associated drag payload.
- `containerNamespace`: A namespace of the associated drag container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(containeritemid:containernamespace:))*