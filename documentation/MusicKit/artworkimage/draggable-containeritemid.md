# draggable(containerItemID:)

**Framework**: MusicKit  
**Kind**: method

Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func draggable<ItemID>(containerItemID: ItemID) -> some View where ItemID : Hashable, ItemID : Sendable
```

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

This modifier marks the view as a draggable element of an enclosing `dragContainer(_:_:)`. Since this modifier does not require to provide the payload, only its identifier, it can works\ lazily (the framework calls the `dragContainer(_:_:)`’s `payload` closure only when drag starts).

Applying the `draggable(containerItemID:)` modifier adds the appropriate gestures for drag and drop to this view. SwiftUI generates a default drag preview for drag.

Below, each `FruitView` is assigned an identifier: the code of the fruit it represents. When dragging begins, the `dragContainer(_:_:)`’s `payload` closure is called with the codes of the selected fruit, or, if a user drags a view that is not selected, the closure receives the identifier of that view as a parameter.

```swift
       struct FruitContainerView: View {
           var fruits: [Fruit]
           var selectedFruits: [UUID]

           var body: some View {
               VStack {
                   ForEach(fruits) { fruit in
                       .draggable(containerItemID: fruit.code)
                   }
                   .dragContainer(selection: selectedFruits) { identifiers in
                       fruits(ids: identifiers)
                   }
               }
           }
           /// Returns fruits with given identifiers.
           func fruits(ids: [UUID]) -> [Fruit] { ... }
       }

       struct Fruit: Transferable {
           var code: UUID
           ...
       }
```

## Parameters

- `containerItemID`: An identifier of the associated drag payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/draggable(containeritemid:))*