---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocksimplecontactview"
framework: "CareKit/CareKitUI"
---

# OCKSimpleContactView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays information for a contact. The header is an `OCKHeaderView`.

## Declaration

```swift
@MainActor
class OCKSimpleContactView
```

#### Overview

```
    +-------------------------------------------------------+
    | +------+                                              |
    | | icon | [title]                       [detail        |
    | | img  | [detail]                       disclosure]   |
    | +------+                                              |
    +-------------------------------------------------------+
```

## Topics

### Instance Properties
- [let contentStackView: OCKStackView](./ocksimplecontactview/contentstackview.md)
  A vertical stack view that holds the main content in the view.
- [var delegate: OCKContactViewDelegate?](./ocksimplecontactview/delegate.md)
  An object that handles events related to a contact object.
- [let headerView: OCKHeaderView](./ocksimplecontactview/headerview.md)
  A header stack view that shows an icon image view and a separator.
### Instance Methods
- [func styleDidChange()](./ocksimplecontactview/styledidchange%28%29.md)

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
- [OCKContactDisplayable](./ockcontactdisplayable.md)
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

### Contacts
- [class OCKDetailedContactView](./ockdetailedcontactview.md)
  A card that displays information for a contact.
- [class OCKAddressButton](./ockaddressbutton.md)
- [class OCKContactButton](./ockcontactbutton.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocksimplecontactview)*