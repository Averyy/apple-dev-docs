# dragConfiguration(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures a drag session.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func dragConfiguration(_ configuration: DragConfiguration) -> some View
```

#### Return Value

A view that configures a drag session in a way, described by the `configuration` parameter.

#### Discussion

Below is a simplified example of a view that supports copy, move and delete operations for drag.

##### Drag to Delete Into Trash Bin

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

- `configuration`: A value that describes the configuration   of a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dragconfiguration(_:))*