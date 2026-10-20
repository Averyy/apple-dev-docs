# NSCollectionLayoutSpacing

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that defines the space between or around items in a collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutSpacing
```

```objc
@interface NSCollectionLayoutSpacing : NSObject
```

#### Overview

In a collection view layout, you use a spacing object to specify both the amount of space and the way in which it’s calculated.

You can express spacing using fixed or flexible spacing.

Use *fixed spacing* to provide an exact amount of space. For example, the following code creates exactly 200 points of space between the items in the group.

**Swift**:

```swift
group.interItemSpacing = .fixed(200.0)
```

**Objective-C**:

```objc
[group setInterItemSpacing: [NSCollectionLayoutSpacing fixedSpacing:200.0]];
```

Use *flexible spacing* to provide a minimum amount of space that can grow as more space becomes available. For example, the following code creates at least 200 points of space between the items in the group. As more space becomes available, items are respaced evenly in the additional space.

**Swift**:

```swift
group.interItemSpacing = .flexible(200.0)
```

**Objective-C**:

```objc
[group setInterItemSpacing: [NSCollectionLayoutSpacing flexibleSpacing:200.0]];
```

## Topics

### Creating spacing
- [class func fixed(CGFloat) -> Self](./nscollectionlayoutspacing/fixed%28_%29.md)
  Creates a space equivalent to the specified number of points.
- [class func flexible(CGFloat) -> Self](./nscollectionlayoutspacing/flexible%28_%29.md)
  Creates a space equivalent to or greater than the specified number of points, depending on the available space.
### Getting the spacing value
- [var spacing: CGFloat](./nscollectionlayoutspacing/spacing.md)
  The floating-point value of the space.
### Getting the spacing type
- [var isFixed: Bool](./nscollectionlayoutspacing/isfixed.md)
  A Boolean value that indicates whether the space is fixed to a specific number of points.
- [var isFlexible: Bool](./nscollectionlayoutspacing/isflexible.md)
  A Boolean value that indicates whether the space is flexible.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Size and spacing
- [class NSCollectionLayoutDimension](./nscollectionlayoutdimension.md)
  An individual dimension representing an item’s width or height in a collection view.
- [class NSCollectionLayoutSize](./nscollectionlayoutsize.md)
  The width and the height of an item in a collection view.
- [class NSCollectionLayoutEdgeSpacing](./nscollectionlayoutedgespacing.md)
  An object that defines the space around the edges of items in a collection view.
- [protocol NSCollectionLayoutContainer](./nscollectionlayoutcontainer.md)
  A protocol used to provide information about the size and content insets of a layout’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutspacing)*