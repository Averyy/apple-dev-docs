# UICollectionViewCompositionalLayoutConfiguration

**Framework**: UIKit  
**Kind**: class

An object that defines scroll direction, section spacing, and headers or footers for the layout.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewCompositionalLayoutConfiguration
```

#### Overview

You use a layout configuration to modify a collection view layout’s default scroll direction, add extra spacing between each section of the layout, and add headers or footers to the entire layout.

You can pass in this configuration when creating a [`UICollectionViewCompositionalLayout`](uicollectionviewcompositionallayout.md), or you can set the [`configuration`](uicollectionviewcompositionallayout/configuration.md) property on an existing layout. If you modify the configuration on an existing layout, the system invalidates the layout so that it will be updated with the new configuration.

## Topics

### Specifying scroll direction
- [var scrollDirection: UICollectionView.ScrollDirection](uicollectionviewcompositionallayoutconfiguration/scrolldirection.md)
  The axis that the content in the collection view layout scrolls along.
### Configuring spacing
- [var interSectionSpacing: CGFloat](uicollectionviewcompositionallayoutconfiguration/intersectionspacing.md)
  The amount of space between the sections in the layout.
- [var contentInsetsReference: UIContentInsetsReference](uicollectionviewcompositionallayoutconfiguration/contentinsetsreference.md)
  The boundary to reference when defining content insets.
- [enum UIContentInsetsReference](uicontentinsetsreference.md)
  Constants that describe the reference point of the content insets.
### Configuring additional views
- [var boundarySupplementaryItems: [NSCollectionLayoutBoundarySupplementaryItem]](uicollectionviewcompositionallayoutconfiguration/boundarysupplementaryitems.md)
  An array of the supplementary items that are associated with the boundary edges of the entire layout, such as global headers and footers.

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

- [typealias UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.
- [protocol NSCollectionLayoutEnvironment](nscollectionlayoutenvironment.md)
  A protocol used to provide information about the layout’s container and environment traits, such as size classes and display scale factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayoutconfiguration)*