# dragConfiguration(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures a drag session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 26.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
func dragConfiguration(_ configuration: DragConfiguration) -> some View
```

#### Return Value

A view that configures a drag session in a way, described by the `configuration` parameter.

#### Discussion

Below is a simplified example of a view that supports copy, move and delete operations for drag.

##### Drag to delete into trash bin

If a view wants to support drag-to-delete into the trash bin or another location that has similar semantics, it should specify the support for this operation in a drag configuration:

```swift
    @State private var photos: [Photo] = []
    @State private var selectedPhotos: [Photo.ID] = []

    var body: some View {
        ScrollView {
            LazyVGrid(columns: gridColumns) {
                ForEach(photos) { photo in
                    PhotoView(photo: photo)
                        .draggable(containerItemID: photo.id)
                }
            }
        }
        .dragContainer(for: Photo.self) { draggedIDs in
            photos(ids: draggedIDs)
        }
        .dragContainerSelection(selectedPhotos)
        .dragConfiguration(DragConfiguration(allowMove: false, allowDelete: true))
        .onDragSessionUpdated { session in
            if session.phase == .ended(.delete) {
                let ids = session.draggedItemIDs(for: Photo.ID.self)
                removeAndTrash(ids)
            }
        }
        .dragPreviewsFormation(.stack)
    }

    func removeAndTrash(_ ids: [Photo.ID]) {
        ids.forEach { id
            if let idx = photos.firstIndex(where: { $0.id == id }) {
                let photo = photos[idx]
                photos.remove(at: idx)
                try? FileManager.default.trashItem(
                    at: photo.fileURL, resultingItemURL: nil
                )
            }
        }
    }
}
```

Note, that any drag supports copy operation by default. In the snippet above, the view supports both copy and delete operations.

## Parameters

- `configuration`: A value that describes the configuration of a drag session.

## See Also

### Configuring drag-and-drop behavior
- [struct DragConfiguration](../dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](./dropconfiguration%28_%29.md)
  Configures a drop session.
- [struct DropConfiguration](../dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:in:_:)](./dragcontainer%28for,in,_%29.md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](./dragcontainer%28for,itemid,in,_%29.md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](./dragcontainerselection%28_,containernamespace%29.md)
  Provides multiple item selection support for drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dragconfiguration(_:))*