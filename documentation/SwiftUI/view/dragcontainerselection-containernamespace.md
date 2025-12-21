# dragContainerSelection(_:containerNamespace:)

**Framework**: SwiftUI  
**Kind**: method

Provides multiple item selection support for drag containers.

**Availability**:
- macOS 26.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dragcontainerselection(_:containernamespace:))*