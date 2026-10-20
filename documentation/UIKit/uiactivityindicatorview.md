# UIActivityIndicatorView

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A view that shows that a task is in progress.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIActivityIndicatorView
```

```objc
@interface UIActivityIndicatorView : UIView
```

#### Overview

You control when an activity indicator animates by calling the [`startAnimating()`](./uiactivityindicatorview/startanimating%28%29.md) and [`stopAnimating()`](./uiactivityindicatorview/stopanimating%28%29.md) methods. To automatically hide the activity indicator when animation stops, set the [`hidesWhenStopped`](./uiactivityindicatorview/hideswhenstopped.md) property to [`true`](../Swift/true.md).

You can set the color of the activity indicator by using the [`color`](./uiactivityindicatorview/color.md) property.

## Topics

### Creating an activity indicator
- [init(style: UIActivityIndicatorView.Style)](./uiactivityindicatorview/init%28style%29.md)
  Creates an activity indicator.
- [init(frame: CGRect)](./uiactivityindicatorview/init%28frame%29.md)
  Creates an activity indicator with the specified frame rectangle.
- [init(coder: NSCoder)](./uiactivityindicatorview/init%28coder%29.md)
  Creates an activity indicator from data in an unarchiver.
### Managing an activity indicator
- [func startAnimating()](./uiactivityindicatorview/startanimating%28%29.md)
  Starts the animation of the progress indicator.
- [func stopAnimating()](./uiactivityindicatorview/stopanimating%28%29.md)
  Stops the animation of the progress indicator.
- [var isAnimating: Bool](./uiactivityindicatorview/isanimating.md)
  A Boolean value indicating whether the activity indicator is currently running its animation.
- [var hidesWhenStopped: Bool](./uiactivityindicatorview/hideswhenstopped.md)
  A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.
### Configuring the activity indicator appearance
- [var style: UIActivityIndicatorView.Style](./uiactivityindicatorview/style-swift.property.md)
  The basic appearance of the activity indicator.
- [var color: UIColor!](./uiactivityindicatorview/color.md)
  The color of the activity indicator.
### Constants
- [UIActivityIndicatorView.Style](./uiactivityindicatorview/style-swift.enum.md)
  The visual style of the progress indicator.
### Initializers
- [init(activityIndicatorStyle: UIActivityIndicatorView.Style)](./uiactivityindicatorview/init%28activityindicatorstyle%29.md)

## Relationships

### Inherits From
- [UIView](./uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](./uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](./uiactivityitemsconfigurationproviding.md)
- [UIAppearance](./uiappearance.md)
- [UIAppearanceContainer](./uiappearancecontainer.md)
- [UICoordinateSpace](./uicoordinatespace.md)
- [UIDynamicItem](./uidynamicitem.md)
- [UIFocusEnvironment](./uifocusenvironment.md)
- [UIFocusItem](./uifocusitem.md)
- [UIFocusItemContainer](./uifocusitemcontainer.md)
- [UILargeContentViewerItem](./uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](./uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](./uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](./uiresponderstandardeditactions.md)
- [UITraitChangeObservable](./uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](./uitraitenvironment.md)
- [UIUserActivityRestoring](./uiuseractivityrestoring.md)

## See Also

### Content views
- [class UICalendarView](./uicalendarview.md)
  A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [class UIContentUnavailableView](./uicontentunavailableview.md)
  A view that indicates there’s no content to display.
- [class UIImageView](./uiimageview.md)
  A view that displays a single image or a sequence of animated images in your interface.
- [class UIPickerView](./uipickerview.md)
  A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
- [class UIProgressView](./uiprogressview.md)
  A view that depicts the progress of a task over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview)*