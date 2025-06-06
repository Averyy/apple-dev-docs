# NSCollectionLayoutSpacing

**Framework**: UIKit  
**Kind**: class

An object that defines the space between or around items in a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSCollectionLayoutSpacing
```

#### Overview

In a collection view layout, you use a spacing object to specify both the amount of space and the way in which it’s calculated.

You can express spacing using fixed or flexible spacing.

Use  to provide an exact amount of space. For example, the following code creates exactly 200 points of space between the items in the group.

Use  to provide a minimum amount of space that can grow as more space becomes available. For example, the following code creates at least 200 points of space between the items in the group. As more space becomes available, items are respaced evenly in the additional space.

## Topics

### Creating spacing
- [class func fixed(CGFloat) -> Self](nscollectionlayoutspacing/fixed(_:).md)
  Creates a space equivalent to the specified number of points.
- [class func flexible(CGFloat) -> Self](nscollectionlayoutspacing/flexible(_:).md)
  Creates a space equivalent to or greater than the specified number of points, depending on the available space.
### Getting the spacing value
- [var spacing: CGFloat](nscollectionlayoutspacing/spacing.md)
  The floating-point value of the space.
### Getting the spacing type
- [var isFixed: Bool](nscollectionlayoutspacing/isfixed.md)
  A Boolean value that indicates whether the space is fixed to a specific number of points.
- [var isFlexible: Bool](nscollectionlayoutspacing/isflexible.md)
  A Boolean value that indicates whether the space is flexible.

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

- [class NSCollectionLayoutDimension](nscollectionlayoutdimension.md)
  An individual dimension representing an item’s width or height in a collection view.
- [class NSCollectionLayoutSize](nscollectionlayoutsize.md)
  The width and the height of an item in a collection view.
- [class NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md)
  An object that defines the space around the edges of items in a collection view.
- [protocol NSCollectionLayoutContainer](nscollectionlayoutcontainer.md)
  A protocol used to provide information about the size and content insets of a layout’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutspacing)*