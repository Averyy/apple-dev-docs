# NSCollectionLayoutGroupCustomItem

**Framework**: AppKit  
**Kind**: class

An item used in a group with a custom layout arrangement.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutGroupCustomItem
```

#### Overview

You use a custom item if you want to specify a layout with a custom arrangement, like a radial or diagonal layout. You use custom items within a group that’s created with [`custom(layoutSize:itemProvider:)`](nscollectionlayoutgroup/custom(layoutsize:itemprovider:).md).

Instead of providing a layout size for the custom item, like you do when you create an [`NSCollectionLayoutItem`](nscollectionlayoutitem.md), you provide a frame instead.

## Topics

### Creating a custom item
- [convenience init(frame: NSRect)](nscollectionlayoutgroupcustomitem/init(frame:).md)
  Creates a custom item with the specified frame.
- [convenience init(frame: NSRect, zIndex: Int)](nscollectionlayoutgroupcustomitem/init(frame:zindex:).md)
  Creates a custom item with the specified frame and vertical stacking order in relation to other items in the group.
### Getting the frame
- [var frame: NSRect](nscollectionlayoutgroupcustomitem/frame.md)
  The frame of the custom item.
### Specifying stacking order
- [var zIndex: Int](nscollectionlayoutgroupcustomitem/zindex.md)
  The vertical stacking order of the custom item in relation to other items in the group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias NSCollectionLayoutGroupCustomItemProvider](nscollectionlayoutgroupcustomitemprovider.md)
  A closure that creates and returns each of the custom group’s items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroupcustomitem)*