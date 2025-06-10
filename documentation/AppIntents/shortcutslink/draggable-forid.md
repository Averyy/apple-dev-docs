# draggable(for:id:_:)

**Framework**: App Intents  
**Kind**: method

Activates this view as the source of a drag-and-drop operation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func draggable<T, ID>(for type: T.Type = T.self, id: ID, _ payload: @escaping (ID) -> T?) -> some View where T : Transferable, ID : Hashable, ID : Sendable
```

#### Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input. If the closure returns `nil`, the drag operation doesn’t start.

#### Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a `View/contentShape(_:_:eoFill:)` with a `ContentShapeKinds/dragPreview` kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

Below is an example view that disables drag when `allowDragging` binding is `false`.

```swift
   @Binding var allowDragging: Bool
   var fruits: [Fruit]
   var selectedFruits: [UUID]

   var body: some View {
       ScrollView {
           VStack {
               ForEach(fruits) { fruit in
                   FruitView(fruit)
                       .draggable(for: Fruit.self, id: fruit.code) { draggedFruitID in
                           allowDragging ? fruit(id: draggedFruitID) : nil
                       }
               }
           }
       }
       .dragContainer(selection: selectedFruits) { identifiers in
           fruits(ids: identifiers)
       }
       .padding()
   }

   /// Returns a fruit with given identifier if it exists.
   func fruit(id: UUID) -> Fruit? { ... }

   struct Fruit: Transferable {
       var code: UUID
       ...
    }
```

## Parameters

- `type`: A the type of the dragged payload.
- `id`: A unique identifier of the dragged item.
- `payload`: A closure that returns a single   instance or a value conforming to   that   represents the draggable data from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/draggable(for:id:_:))*