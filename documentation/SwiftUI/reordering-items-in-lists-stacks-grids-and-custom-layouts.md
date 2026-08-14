# Reordering items in lists, stacks, grids, and custom layouts

**Framework**: SwiftUI

Add drag-to-reorder interactions to SwiftUI layouts using reordering modifiers.

#### Overview

SwiftUI provides reordering when you have one or more collections of ordered data items, each displayed as a view in a *container*, such as a list, stack, grid, or custom layout. The system lets someone select a view that represents a data item and drag it around the container. As they drag the view, other views move to show a placeholder space where the person can drop the view.

When the person drops the view on the placeholder, the system provides the identifiers of the data items that correspond to the moving views along with the new position for the views. Then, you can move the data items that correspond to the moving views in your collection, even if other changes to the array, such as a cloud sync, occur simultaneously.

If you organize your views into sections that you represent in multiple data collections, such as a photography app that lets people organize photos into albums, you can configure reordering to work both when someone moves a photo inside an album and when someone moves a photo from one album to another.

##### Reorder Items in a Single Collection

When you have views that you build from a single ordered collection of data items, such as an array of photos in a photography app, first configure your data item with an identifier that conforms to [`Hashable`](https://developer.apple.com/documentation/swift/hashable) and [`Sendable`](https://developer.apple.com/documentation/swift/sendable). For example, update your data item to conform to  [`Identifiable`](https://developer.apple.com/documentation/swift/identifiable) using an identifier data type that conforms to [`Sendable`](https://developer.apple.com/documentation/swift/sendable).

Next, indicate which views you want people to reorder by adding the [`reorderable()`](dynamicviewcontent/reorderable().md) modifier to the [`ForEach`](foreach.md) declaration that generates those views, as the following code shows:

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ForEach(photos) { photo in
            PhotoView(photo: photo)
        }
        .reorderable()
    }
}
```

Finally, define the area in your interface where people can reorder views by adding the [`reorderContainer(for:isEnabled:move:)`](view/reordercontainer(for:isenabled:move:).md) modifier to the enclosing list, stack, grid, or custom layout container to specify the scope of views to include in reordering. In the `move` closure, specify how to apply the [`ReorderDifference`](reorderdifference.md) that the system provides to describe the change to your collection of items, as this code example shows:

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ...
    }
    .reorderContainer(for: Photo.self) { difference in
        move(difference: difference)
    }
}
```

##### Reorder Items Across Multiple Collections

When you organize your views into sections that you build from multiple data collections, such as albums in a photography app that each contain photos, add [`reorderable(collectionID:)`](dynamicviewcontent/reorderable(collectionid:).md) to the [`ForEach`](foreach.md) that generates the views you want to reorder. Then, provide an identifier for each collection that contains the data items for those views, as this example shows:

```swift
ScrollView {
    LazyVStack {
        ForEach(model.albumSections) { albumSection in
            Section(albumSection.title) {
                ForEach(albumSection.items) { photo in
                    PhotoView(photo: photo)
                }
                .reorderable(collectionID: albumSection.id)
            }
        }
    }
}
```

Next, define the scope of the reordering area by adding [`reorderContainer(for:in:isEnabled:move:)`](view/reordercontainer(for:in:isenabled:move:).md) to the list, stack, grid, or custom layout that contains all of the sections and views you want to reorder:

```swift
ScrollView {
    LazyVStack {
        ...
    }
    .reorderContainer(
        for: Photo.self,
        in: AlbumSection.ID.self
    ) { difference in
        move(difference: difference)
    }
}
```

When someone moves a view inside an album, or from one album to another, the system provides a [`ReorderDifference`](reorderdifference.md) instance that contains a collection identifier and position you can use to move the view’s corresponding data item.

##### Support Drag and Drop Outside Your Container

Adding reordering modifiers to your container only supports moving views inside the container. Support drag and drop between your container and other parts of your app or other apps with drag-and-drop modifiers.

Add the [`dragContainer(for:in:_:)`](view/dragcontainer(for:in:_:).md) modifier to provide transfer representations for views when someone drags them outside of your container. For example, the following code shows how to select a `Photo` instance the system can use to get a transfer representation when someone drags a photo to another window or app:

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ...
    }
    .reorderContainer(for: Photo.self) { difference in
        move(difference: difference)
    }
    .dragContainer(for: Photo.self) { photoID in
        guard let photo = photos.first(where: { $0.id == photoID }) else {
            return []
        }
        return [photo]
    }
}
```

Add the [`dropDestination(for:isEnabled:action:)`](view/dropdestination(for:isenabled:action:).md) modifier after the [`reorderContainer(for:isEnabled:move:)`](view/reordercontainer(for:isenabled:move:).md) modifier to handle drop actions from other parts of your app or other apps. When the drop destination modifier encloses the reorder container modifier, the container handles drag-and-drop reordering operations inside the container, and the drop destination handles drag-and-drop operations that someone initiates outside the container.

Inside the drop action closure, call [`reorderDestination(for:in:)`](dropsession/reorderdestination(for:in:).md) to find where the person dropped the views relative to existing views. In the following example, when the method returns [`ReorderDifference.Destination.Position.before(_:)`](reorderdifference/destination-swift.struct/position-swift.enum/before(_:).md), that indicates someone dropped one or more `Photo` representations before the view represented by the `Photo` instance at `index`. In that case, you insert the dropped items before the item at `index`. When the method returns [`ReorderDifference.Destination.Position.end`](reorderdifference/destination-swift.struct/position-swift.enum/end.md), someone dropped one or more `Photo` representations after the last view, so you append the dropped items to the end of the collection. The following code demonstrates both of these examples:

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ...
    }
    .reorderContainer(for: Photo.self) { difference in
        move(difference: difference)
    }
    .dragContainer(for: Photo.self) { photoID in
        guard let photo = photos.first(where: { $0.id == photoID }) else {
            return []
        }
        return [photo]
    }
    .dropDestination(for: Photo.self) { items, session in
        if let destination = session.reorderDestination(for: Photo.ID.self),
           let index = model.index(for: destination) {
            photos.insert(contentsOf: items, at: index)
        } else {
            photos.append(contentsOf: items)
        }
        return true
    }
}
```

##### Support Drag and Drop Onto Individual Items in a Reorderable Container

Add the [`dropDestination(for:isEnabled:action:)`](view/dropdestination(for:isenabled:action:).md) modifier to an item’s view to let people drop items from other apps directly onto a specific item in your container. The following code shows how to add the drop destination to an `ItemView` inside a `ForEach` that’s also configured for reordering:

```swift
HStack {
    ForEach(items) { item in
        ItemView(item)
            .dropDestination(for: Item.self, isEnabled: item.isFolder) { newItems, destination in ... }
    }
    .reorderable()
}
.reorderContainer(for: Item.self) { difference in ... }
```

Use the `isEnabled` parameter of the [`dropDestination(for:isEnabled:action:)`](view/dropdestination(for:isenabled:action:).md) modifier to limit what items the drop destination takes. The previous code example shows how to accept drops only when the `isFolder` property for an item is `true`.

Add code in the `action` closure of the [`dropDestination(for:isEnabled:action:)`](view/dropdestination(for:isenabled:action:).md) modifier to update your model with the dropped items, because it may be different than how you handle updating your model for reordering in the closure for [`reorderContainer(for:isEnabled:move:)`](view/reordercontainer(for:isenabled:move:).md). When your drop destination accepts items from the reorder container, be sure to remove the items from the source data collection when you move them to the item’s data collection.

##### Dynamically Enable and Disable Reordering

You may want to disable reordering while you sync updates over the network, or when you make other updates to your views that complicate reordering. To do this, use a variant of the reorder container modifier that has the `isEnabled` parameter, and pass a Boolean property to that parameter to track whether reordering is enabled, as the following example shows:

```swift
ScrollView {
    LazyVStack {
        ...
    }
    .reorderContainer(
        for: Photo.self,
        isEnabled: !model.isSaving
    ) { difference in
        model.apply(difference: difference)
    }
}
```

In that example, reordering is disabled when `isSaving` is `true`. When the model completes saving and changes `isSaving` to `false`, reordering is enabled.

## See Also

- [Adopting drag and drop using SwiftUI](adopting-drag-and-drop-using-swiftui.md)
  Enable drag-and-drop interactions in lists, tables and custom views.
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
  Adopt draggable API to provide items for drag-and-drop operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reordering-items-in-lists-stacks-grids-and-custom-layouts)*