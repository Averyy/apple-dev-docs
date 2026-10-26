---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdetailview"
framework: "CareKit/CareKitUI"
---

# OCKDetailView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A scrollable view with an image header and text content.

## Declaration

```swift
@MainActor
class OCKDetailView
```

#### Overview

Use `contentStackView` to insert custom views.

```
    +-------------------------------------------------------+
    |                                                       |
    |                        <Image>                        |
    |   <Image Label>                                       |
    |-------------------------------------------------------|
    |   <Title>                                             |
    |   <Body>                                              |
    |                                                       |
    |                                                       |
    +-------------------------------------------------------+
```

## Topics

### Structures
- [OCKDetailView.StyledHTML](./ockdetailview/styledhtml.md)
  String representations of HTML and CSS for styling.
### Initializers
- [init(html: StyledHTML?, imageOverlayStyle: UIUserInterfaceStyle, showsCloseButton: Bool)](./ockdetailview/init%28html,imageoverlaystyle,showsclosebutton%29.md)
  Create an instance.
### Instance Properties
- [let bodyLabel: OCKLabel](./ockdetailview/bodylabel.md)
  Secondary label.
- [var closeButton: UIButton?](./ockdetailview/closebutton.md)
  Close button. The button will be non-nil when `showsCloseButton` is true.
- [let contentStackView: OCKStackView](./ockdetailview/contentstackview.md)
  Holds the main content.
- [var html: StyledHTML?](./ockdetailview/html.md)
  HTML to render in the `bodyLabel`.
- [var imageLabel: OCKLabel](./ockdetailview/imagelabel.md)
  Label overlaying the header image.
- [var imageView: UIImageView](./ockdetailview/imageview.md)
  Header image.
- [let titleLabel: OCKLabel](./ockdetailview/titlelabel.md)
  Primary label.
### Instance Methods
- [func layoutSubviews()](./ockdetailview/layoutsubviews%28%29.md)
- [func scrollViewDidScroll(UIScrollView)](./ockdetailview/scrollviewdidscroll%28_%29.md)
- [func styleDidChange()](./ockdetailview/styledidchange%28%29.md)
- [func traitCollectionDidChange(UITraitCollection?)](./ockdetailview/traitcollectiondidchange%28_%29.md)

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
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
- UIKit.UIScrollViewDelegate
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring
- UIUtilities.UICoordinateSpace


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdetailview)*