# onDragSessionUpdated(_:)

**Framework**: FamilyControls  
**Kind**: method

Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or other drag modifiers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
                   configuration: .init(
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/ondragsessionupdated(_:))*