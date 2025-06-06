# NSCollectionLayoutEnvironment

**Framework**: UIKit  
**Kind**: protocol

A protocol used to provide information about the layout’s container and environment traits, such as size classes and display scale factor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol NSCollectionLayoutEnvironment : NSObjectProtocol
```

#### Overview

In a section provider, you use the layout environment to get information about the context that the layout appears in. You can get information about the layout’s container, such as its size and content insets, and the traits of its environment, such as size classes, display scale factor, and user interface idiom. You use this information while rendering the layout’s sections to help you make decisions about how to display the layout.

For example, the following code uses the layout environment’s trait collection to check whether the UI is in Dark Mode while creating the layout’s sections.

## Topics

### Getting the layout’s container
- [var container: any NSCollectionLayoutContainer](nscollectionlayoutenvironment/container.md)
  Information about the layout’s container, such as its size and content insets.
### Getting the trait collection
- [var traitCollection: UITraitCollection](nscollectionlayoutenvironment/traitcollection.md)
  The traits that describe the current environment of the layout, such as the size classes and display scale factor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UICollectionViewCompositionalLayoutConfiguration](uicollectionviewcompositionallayoutconfiguration.md)
  An object that defines scroll direction, section spacing, and headers or footers for the layout.
- [typealias UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutenvironment)*