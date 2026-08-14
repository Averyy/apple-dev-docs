# draggable(_:id:containerNamespace:_:)

**Framework**: SwiftUI  
**Kind**: method

Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func draggable<Item, ItemID>(_ itemType: Item.Type = Item.self, id: KeyPath<Item, ItemID>, containerNamespace: Namespace.ID? = nil, _ payload: @escaping () -> Item?) -> some View where Item : Transferable, ItemID : Hashable, ItemID : Sendable
```

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Applying the `draggable(_:id:containerNamespace:_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

```swift
var fruits: [Fruit]

var body: some View {
    ScrollView {
        VStack {
            ForEach(fruits) { fruit in
                FruitView(fruit)
                    .draggable(Fruit.self, id: \.dragID) {
                        fruit.supportsDrag ? fruit : nil
                    }
            }
        }
    }
}

struct Fruit: Transferable {
    var supportsDrag: Bool
    var dragID: UUID
}
```

If the draggable view is enclosed in a container, it participates in container drag-and-drop sessions:

```swift
var fruits: [Fruit]
var selectedFruits: [UUID]

var body: some View {
    ScrollView {
        VStack {
            ForEach(fruits) { fruit in
                FruitView(fruit)
                    .draggable(Fruit.self, id: \.dragID) {
                        fruit.supportsDrag ? fruit : nil
                    }
            }
        }
    }
    .dragContainer(for: Fruit.self) { identifiers in
        fruits(with: identifiers)
    }
    .dragContainerSelection(selectedFruits)
}

func fruits(with: [UUID]) -> [Fruit] { ... }
```

## Parameters

- `itemType`: A type of the dragged item.
- `id`: An key path of the identifier of an item.
- `containerNamespace`: A namespace of the associated drag container.
- `payload`: A closure that returns a single instance or a value conforming to [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) that represents the draggable data from this view.

## See Also

- [func draggable<T>(@autoclosure () -> T) -> some View](view/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](view/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<Item>(Item.Type, containerNamespace: Namespace.ID?, () -> Item?) -> some View](view/draggable(_:containernamespace:_:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](view/draggable(_:id:item:containernamespace:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item>(Item.Type, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](view/draggable(_:item:containernamespace:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID?) -> some View](view/draggable(containeritemid:containernamespace:).md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/draggable(_:id:containernamespace:_:))*