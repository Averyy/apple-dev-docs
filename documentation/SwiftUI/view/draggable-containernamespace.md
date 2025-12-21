# draggable(_:containerNamespace:_:)

**Framework**: SwiftUI  
**Kind**: method

Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func draggable<Item>(_ itemType: Item.Type = Item.self, containerNamespace: Namespace.ID? = nil, _ item: @escaping () -> Item?) -> some View where Item : Transferable, Item : Identifiable, Item.ID : Sendable
```

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Applying the `draggable(_:containerNamespace_:)` modifier adds the appropriate gestures for drag and drop to this view.

```swift
   var fruits: [Fruit]

   var body: some View {
       ScrollView {
           VStack {
               ForEach(fruits) { fruit in
                   FruitView(fruit)
                       .draggable(fruit)
               }
           }
       }
   }

   struct Fruit: Identifiable, Transferable { ... }
```

If the draggable view is enclosed in a container, it participates in container drag-and-drop sessions:

```swift
   var fruits: [Fruit]
   var selectedFruits: [Fruit.ID]

   var body: some View {
       ScrollView {
           VStack {
               ForEach(fruits) { fruit in
                   FruitView(fruit)
                       .draggable(fruit)
               }
           }
       }
       .dragContainer(for: Fruit.self) { identifiers in
           fruits(with: identifiers)
       }
       .dragContainerSelection(selectedFruits)
   }

   func fruits(with: [Fruit.ID]) -> [Fruit] { ... }
   struct Fruit: Identifiable, Transferable { ... }
```

When a drag operation begins, a rendering of this view is generated and used as the preview image.

## Parameters

- `itemType`: A type of the dragged item.
- `containerNamespace`: A namespace of the associated drag container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:containernamespace:_:))*