# dropConfiguration(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures a drop session.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func dropConfiguration(_ configuration: @escaping (DropSession) -> DropConfiguration) -> some View
```

#### Return Value

A view that configures a drop session in a way, described by the return value of the `configuration` parameter.

#### Discussion

Below is an example of a view that accepts drop of `Image` type. The view prefers drop operation `move` in a case when the source supports it (the source will remove the images from its storage after the drop operation). If the source does not support moving images, the destination will make copies.

```swift
       ExampleView()
           .dropDestination(for: Image.self) { images, _ in
               process(images)
           }
           .dropConfiguration { dropSession in
               if dropSession.suggestedOperations.contains(.move) {
                   return DropConfiguration(operation: .move)
               }
               return DropConfiguration(operation: .copy)
           }
```

> **Note**: The closure that provides the configuration is called frequently to allow specifying different operations for different drop locations in a view. Do not perform any expensive calculations in it.

## Parameters

- `configuration`: A value that describes the configuration of a drop session.

## See Also

- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [struct DragConfiguration](dragconfiguration.md)
  The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.
- [func dragContainer(for:in:_:)](view/dragcontainer(for:in:_:).md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](view/dragcontainer(for:itemid:in:_:).md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](view/dragcontainerselection(_:containernamespace:).md)
  Provides multiple item selection support for drag containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dropconfiguration(_:))*