# UIContentUnavailableView

**Framework**: UIKit  
**Kind**: class

A view that indicates there’s no content to display.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIContentUnavailableView
```

#### Overview

Use a content-unavailable view to indicate that your app can’t display content. For example, content may not be available if a search returns no results or your app is loading data over the network.

In many cases, you won’t need to create a view of this type directly. Set a [`UIContentUnavailableConfiguration`](uicontentunavailableconfiguration-swift.struct.md) as the view controller’s [`contentUnavailableConfiguration`](uiviewcontroller/contentunavailableconfiguration-4b95e.md), and the view controller manages the layout of the content-unavailable view.

## Topics

### Initializers
- [init(coder: NSCoder)](uicontentunavailableview/init(coder:).md)
  Creates a view from data in an unarchiver.
- [convenience init(configuration: UIContentUnavailableConfiguration)](uicontentunavailableview/init(configuration:).md)
  Creates a new content-unavailable view with the specified configuration.
### Instance Properties
- [var isScrollEnabled: Bool](uicontentunavailableview/isscrollenabled.md)
  A Boolean value that determines whether the view content can scroll.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentView](uicontentview-5fh3z.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIActivityIndicatorView](uiactivityindicatorview.md)
  A view that shows that a task is in progress.
- [class UICalendarView](uicalendarview.md)
  A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [class UIImageView](uiimageview.md)
  A view that displays a single image or a sequence of animated images in your interface.
- [class UIPickerView](uipickerview.md)
  A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
- [class UIProgressView](uiprogressview.md)
  A view that depicts the progress of a task over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableview)*