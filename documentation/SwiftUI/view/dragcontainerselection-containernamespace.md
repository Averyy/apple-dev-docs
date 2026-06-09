# dragContainerSelection(_:containerNamespace:)

**Framework**: SwiftUI  
**Kind**: method

Provides multiple item selection support for drag containers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func dragContainerSelection<ItemID>(_ selection: @autoclosure @escaping () -> Array<ItemID>, containerNamespace: Namespace.ID? = nil) -> some View where ItemID : Hashable, ItemID : Sendable
```

#### Discussion

A drag container finds the nearest enclosing `dragContainerSelection(_:containerNamespace:)` with the same item identifier type and same namespace, if specified. Drag container uses the provided selected item identifiers to determine what the drag payload should be.

If the dragged view is associated with a selected identifier, the payload should contain all the selected items. If the dragged view is not selected, the payload should not contain the whole selection, just the dragged item. With `dragContainerSelection(_:containerNamespace:)`, you get fine-grained control over what items are included in the drag payload.

```swift
    struct FruitContainer: View {
         @State private var fruits: [Fruit]
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

       func fruits(with ids: [Fruit.ID]) -> [Fruit] { ... }

       struct Fruit: Transferable, Identifiable {
           let id: String
           ...
       }

       struct FruitView: View {
           init(_ fruit: Fruit) { ... }
       }
   }
```

## Parameters

- `selection`: A closure that provides identifiers of selected items.
- `containerNamespace`: An optional namespace of the drag container.

## See Also

- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [struct DragConfiguration](dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:in:_:)](view/dragcontainer(for:in:_:).md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](view/dragcontainer(for:itemid:in:_:).md)
  A container with draggable views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dragcontainerselection(_:containernamespace:))*