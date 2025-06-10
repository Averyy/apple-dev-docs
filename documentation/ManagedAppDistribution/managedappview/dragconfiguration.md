# dragConfiguration(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Configures a drag session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dragConfiguration(_ configuration: DragConfiguration) -> some View
```

#### Return Value

A view that configures a drag session in a way, described by the `configuration` parameter.

#### Discussion

Below is a simplified example of a view that supports copy, move and delete operations for drag.

```None
   struct DraggableBookView: View {
       @Binding var books: [Book]
       var book: Book

       /// Comfigures the drag to support move and delete
       /// operations in addition to copy.
       var dragConfiguration: DragConfiguration {
           DragConfiguration(allowMove: true, allowDelete: true)
       }

       var body: some View {
           BookView()
               .draggable(book)
               .dragConfiguration(dragConfiguration)
               .onDragSessionUpdated { session in
                   switch session.phase {
                   case .ended(let operation):
                       switch operation {
                       case .move:
                           removeFromLibrary(book)
                           onBookMoved(book)
                       case .delete:
                           removeFromLibrary(book)
                           onBookDeleted(book)
                       default: break
                       }
                   default: break
                   }
               }
       }

       func removeFromLibrary(_ book: Book) {
           if let idx = self.books.firstIndex(
               where: { $0.id == book.id }
           ) {
               self.books.remove(at: idx)
           }
       }

       /// If a book was moved somewhere else, it can be removed
       /// from this storage.
       func onBookMoved(_ book: Book) {
           try? FileManager.default.removeItem(at: book.file)
       }

       /// If a dragging session ended with operation delete,
       /// move the book to Trash so that users could
       /// restore it from there.
       func onBookDeleted(_ book: Book) {
           try? FileManager.default.trashItem(
               at: book.file, resultingItemURL: nil
           )
       }
   }

   struct Book: Identifiable, Transferable {
       let id: UUID
       let file: URL
       ...
   }

   struct BookView: View { ... }
```

## Parameters

- `configuration`: A value that describes the cofiguration   of a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/dragconfiguration(_:))*