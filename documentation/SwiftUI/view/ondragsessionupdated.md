# onDragSessionUpdated(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or anther drag modifiers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func onDragSessionUpdated(_ onUpdate: @escaping (DragSession) -> Void) -> some View
```

#### Discussion

Below is an example of a view that displays a book and supports dragging to copy, move, and delete. If the session ends with moving or deleting the item, in the `onUpdate` closure, the view lets the model layer know that the book should be deleted from the source.

```swift
   struct DraggableBookView: View {
       var id: UUID

       var body: some View {
           BookView()
               .draggable(
                   configuration: DragConfiguration(
                       operationsWithinApp: .init(allowMove: true, allowDelete: true),
                       operationsOutsideApp: .init(allowMove: true, allowDelete: true)
                   ), Book(id: id))
               .onDragSessionUpdated { session in
                   switch session.phase {
                   case .ended(at: _, with: let operation):
                       if operation == .move || operation == .delete {
                           if let id = session.draggedItemIDs(type: UUID.self).first {
                               removeBook(id: id)
                           }
                       }
                   default:
                       break
                   }
               }
       }
   }

   func removeBook(id: UUID) { }
```

The `onUpdate` closure is called when the closest drag session in the child view hierarchy becomes active.

## See Also

- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [func dragContainer(for:in:_:)](view/dragcontainer(for:in:_:).md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](view/dragcontainer(for:itemid:in:_:).md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](view/dragcontainerselection(_:containernamespace:).md)
  Provides multiple item selection support for drag containers.
- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](view/dragpreviewsformation(_:).md)
  Describes the way dragged previews are visually composed.
- [func draggable<T>(@autoclosure () -> T) -> some View](view/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](view/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<Item>(Item.Type, containerNamespace: Namespace.ID?, () -> Item?) -> some View](view/draggable(_:containernamespace:_:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, containerNamespace: Namespace.ID?, () -> Item?) -> some View](view/draggable(_:id:containernamespace:_:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](view/draggable(_:id:item:containernamespace:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item>(Item.Type, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](view/draggable(_:item:containernamespace:).md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID?) -> some View](view/draggable(containeritemid:containernamespace:).md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [func dropDestination<T>(for: T.Type, isEnabled: Bool, action: ([T], DropSession) -> Void) -> some View](view/dropdestination(for:isenabled:action:).md)
  Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](view/droppreviewsformation(_:).md)
  Describes the way previews for a drop are composed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondragsessionupdated(_:))*