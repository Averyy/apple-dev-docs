# NSCollectionLayoutDimension

**Framework**: UIKit  
**Kind**: class

An individual dimension representing an item’s width or height in a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSCollectionLayoutDimension
```

#### Overview

Each item in a collection view has an explicit width dimension and height dimension, which combine to define the item’s size ([`NSCollectionLayoutSize`](nscollectionlayoutsize.md)).

You can express an item’s dimensions using an absolute, estimated, or fractional value.

Use an *absolute value* to specify exact dimensions, like a 44 x 44 point square:

**Swift**:

```swift
let absoluteSize = NSCollectionLayoutSize(widthDimension: .absolute(44),
                                         heightDimension: .absolute(44))
```

**Objective-C**:

```objc
NSCollectionLayoutSize *absoluteSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension absoluteDimension:44.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:44.0]];
```

Use an *estimated value* if the size of your content might change at runtime, such as when data is loaded or in response to a change in system font size. You provide an initial estimated size and the system computes the actual value later.

**Swift**:

```swift
let estimatedSize = NSCollectionLayoutSize(widthDimension: .estimated(200),
                                          heightDimension: .estimated(100))
```

**Objective-C**:

```objc
NSCollectionLayoutSize *estimatedSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension estimatedDimension:200.0] heightDimension:[NSCollectionLayoutDimension estimatedDimension:100.0]];
```

Use a *fractional value* to define a value that’s relative to a dimension of the item’s container. This option simplifies specifying aspect ratios. For example, the following item has a width and a height that are both equal to 20% of its container’s width, creating a square that grows and shrinks as the size of its container changes.

**Swift**:

```swift
let fractionalSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.2),
                                           heightDimension: .fractionalWidth(0.2))
```

**Objective-C**:

```objc
NSCollectionLayoutSize *fractionalSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension fractionalWidthDimension:0.2] heightDimension:[NSCollectionLayoutDimension fractionalWidthDimension:0.2]];
```

## Topics

### Creating a dimension
- [class func absolute(CGFloat) -> Self](nscollectionlayoutdimension/absolute(_:).md)
  Creates a dimension with an absolute point value.
- [class func estimated(CGFloat) -> Self](nscollectionlayoutdimension/estimated(_:).md)
  Creates a dimension with an estimated point value.
- [class func fractionalHeight(CGFloat) -> Self](nscollectionlayoutdimension/fractionalheight(_:).md)
  Creates a dimension that is computed as a fraction of the height of the containing group.
- [class func fractionalWidth(CGFloat) -> Self](nscollectionlayoutdimension/fractionalwidth(_:).md)
  Creates a dimension that is computed as a fraction of the width of the containing group.
- [class func uniformAcrossSiblings(estimate: CGFloat) -> Self](nscollectionlayoutdimension/uniformacrosssiblings(estimate:).md)
  Creates a dimension in which each item receives as much room as it requires and grows to match the dimension of its largest sibling.
### Getting the dimension value
- [var dimension: CGFloat](nscollectionlayoutdimension/dimension.md)
  The floating-point value of the dimension.
### Getting the dimension type
- [var isAbsolute: Bool](nscollectionlayoutdimension/isabsolute.md)
  A Boolean value that indicates whether the dimension is expressed as an absolute value.
- [var isEstimated: Bool](nscollectionlayoutdimension/isestimated.md)
  A Boolean value that indicates whether the dimension is expressed as an estimated value.
- [var isFractionalHeight: Bool](nscollectionlayoutdimension/isfractionalheight.md)
  A Boolean value that indicates whether the dimension is expressed as a fraction of its container’s height.
- [var isFractionalWidth: Bool](nscollectionlayoutdimension/isfractionalwidth.md)
  A Boolean value that indicates whether the dimension is expressed as a fraction of its container’s width.
- [var isUniformAcrossSiblings: Bool](nscollectionlayoutdimension/isuniformacrosssiblings.md)
  A Boolean value that indicates whether the dimension grows to match the dimension of its largest sibling.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class NSCollectionLayoutSize](nscollectionlayoutsize.md)
  The width and the height of an item in a collection view.
- [class NSCollectionLayoutSpacing](nscollectionlayoutspacing.md)
  An object that defines the space between or around items in a collection view.
- [class NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md)
  An object that defines the space around the edges of items in a collection view.
- [protocol NSCollectionLayoutContainer](nscollectionlayoutcontainer.md)
  A protocol used to provide information about the size and content insets of a layout’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutdimension)*