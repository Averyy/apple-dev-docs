---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockfeaturedcontentview"
framework: "CareKit/CareKitUI"
---

# OCKFeaturedContentView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays a large background image.

## Declaration

```swift
@MainActor
class OCKFeaturedContentView
```

## Overview

The whole view is tappable.

## Style

The card supports styling using `careKitStyle(_:)`.

## Topics

### Initializers
- [init(imageOverlayStyle: UIUserInterfaceStyle)](./ockfeaturedcontentview/init%28imageoverlaystyle%29.md)
  Create a featured content view.
### Instance Properties
- [var cardView: UIView](./ockfeaturedcontentview/cardview.md)
- [var contentView: UIView](./ockfeaturedcontentview/contentview.md)
- [var delegate: OCKFeaturedContentViewDelegate?](./ockfeaturedcontentview/delegate.md)
  An object that handles events related to the view.
- [var imageView: UIImageView](./ockfeaturedcontentview/imageview.md)
  Large background image.
- [var intrinsicContentSize: CGSize](./ockfeaturedcontentview/intrinsiccontentsize.md)
- [var label: OCKLabel](./ockfeaturedcontentview/label.md)
  Primary multi-line label.
### Instance Methods
- [func styleDidChange()](./ockfeaturedcontentview/styledidchange%28%29.md)
### Default Implementations
- [OCKCardable Implementations](./ockfeaturedcontentview/ockcardable-implementations.md)

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
- [OCKCardable](./ockcardable.md)
- [OCKStylable](./ockstylable.md)
- ObjectiveC.NSObjectProtocol
- QuartzCore.CALayerDelegate
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype
- UIKit.UIAccessibilityIdentification
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearance
- UIKit.UIAppearanceContainer
- UIKit.UIDynamicItem
- UIKit.UIFocusEnvironment
- UIKit.UIFocusItem
- UIKit.UIFocusItemContainer
- UIKit.UILargeContentViewerItem
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIPopoverPresentationControllerSourceItem
- UIKit.UIResponderStandardEditActions
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring
- UIUtilities.UICoordinateSpace

## See Also

### Featured content
- [protocol OCKFeaturedContentViewDelegate](./ockfeaturedcontentviewdelegate.md)
  Handles events for an `OCKFeaturedContentView`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockfeaturedcontentview)*