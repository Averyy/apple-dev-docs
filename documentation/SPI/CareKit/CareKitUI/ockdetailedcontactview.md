---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdetailedcontactview"
framework: "CareKit/CareKitUI"
---

# OCKDetailedContactView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays information for a contact.

## Declaration

```swift
@MainActor
class OCKDetailedContactView
```

#### Overview

The header is an `OCKHeaderView`. The body contains a multi-line instructions label, and four buttons; call, message, email, and address. The first three buttons have title labels and image views that can be modified, while the last has a title label, body label, and image view.

## Topics

### Instance Properties
- [let addressButton: OCKAddressButton](./ockdetailedcontactview/addressbutton.md)
  A button with a location image, title and detail labels.
- [let callButton: OCKContactButton](./ockdetailedcontactview/callbutton.md)
  A button with a phone image and title label.
- [let contentStackView: OCKStackView](./ockdetailedcontactview/contentstackview.md)
  A vertical stack view that holds the main content in the view.
- [var delegate: OCKContactViewDelegate?](./ockdetailedcontactview/delegate.md)
  An object that handles contact object events.
- [let emailButton: OCKContactButton](./ockdetailedcontactview/emailbutton.md)
  A button with an email image and title label.
- [let headerView: OCKHeaderView](./ockdetailedcontactview/headerview.md)
  Header stack view that shows an icon image view and a separator.
- [let instructionsLabel: OCKLabel](./ockdetailedcontactview/instructionslabel.md)
  The multi-line label under the header view.
- [let messageButton: OCKContactButton](./ockdetailedcontactview/messagebutton.md)
  A button with a messages image and title label.
### Instance Methods
- [func styleDidChange()](./ockdetailedcontactview/styledidchange%28%29.md)
- [func traitCollectionDidChange(UITraitCollection?)](./ockdetailedcontactview/traitcollectiondidchange%28_%29.md)
### Type Properties
- [static let defaultImage: UIImage](./ockdetailedcontactview/defaultimage.md)
  The default image you use as a placeholder for the icon image view in the header view.

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
- [class OCKSimpleContactView](./ocksimplecontactview.md)
  A card that displays information for a contact. The header is an `OCKHeaderView`.
- [class OCKAddressButton](./ockaddressbutton.md)
- [class OCKContactButton](./ockcontactbutton.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdetailedcontactview)*