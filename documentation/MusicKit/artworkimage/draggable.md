# draggable(_:_:)

**Framework**: MusicKit  
**Kind**: method

Activates this view as the source of a drag and drop operation. A view can be dragged separately, or as an element of a drag container.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func draggable<Item>(_ itemType: Item.Type, _ payload: @autoclosure @escaping () -> Item?) -> some View where Item : Transferable, Item : Identifiable, Item.ID : Sendable
```

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

#### Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

Dragging this view starts a drag session. When it is enclosed in a `dragContainer(:_:_)`, the view becomes its draggable element.

To customize the default preview, use the `dragPreview(_:)` modifier, or apply a `View/contentShape(_:_:eoFill:)` with a `ContentShapeKinds/dragPreview` kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

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
       .dragContainer(selection: selectedFruits) { identifiers in
           fruits(ids: identifiers)
       }
       .padding()
   }

   /// Returns fruits with given identifiers.
   func fruits(ids: [Fruit.ID]) -> [Fruit] { ... }

   struct Fruit: Identifiable, Transferable { ... }
```

## Parameters

- `itemType`: A type of the dragged item.
- `payload`: A closure that returns a single   instance or a value conforming to   that   represents the draggable data from this view. If the closure returns  ,   drag is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/draggable(_:_:))*