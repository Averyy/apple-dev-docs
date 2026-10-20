# UIProgressView

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A view that depicts the progress of a task over time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIProgressView
```

```objc
@interface UIProgressView : UIView
```

#### Overview

The [`UIProgressView`](./uiprogressview.md) class provides properties for managing the style of the progress bar and for getting and setting values that are pinned to the progress of a task.

For an indeterminate progress indicator — or a “spinner” — use an instance of the [`UIActivityIndicatorView`](./uiactivityindicatorview.md) class.

## Topics

### Creating a progress view
- [convenience init(progressViewStyle: UIProgressView.Style)](./uiprogressview/init%28progressviewstyle%29.md)
  Creates a progress view with the specified style.
- [init(frame: CGRect)](./uiprogressview/init%28frame%29.md)
  Creates a progress view with the specified frame rectangle.
- [init?(coder: NSCoder)](./uiprogressview/init%28coder%29.md)
  Creates a progress view from data in an unarchiver.
### Managing the progress bar
- [var progress: Float](./uiprogressview/progress.md)
  The current progress of the progress view.
- [func setProgress(Float, animated: Bool)](./uiprogressview/setprogress%28_,animated%29.md)
  Adjusts the current progress of the progress view, optionally animating the change.
- [var observedProgress: Progress?](./uiprogressview/observedprogress.md)
  The progress object to use for updating the progress view.
### Configuring the progress bar
- [var progressViewStyle: UIProgressView.Style](./uiprogressview/progressviewstyle.md)
  The current graphical style of the progress view.
- [var progressTintColor: UIColor?](./uiprogressview/progresstintcolor.md)
  The color shown for the portion of the progress bar that’s filled.
- [var progressImage: UIImage?](./uiprogressview/progressimage.md)
  An image to use for the portion of the progress bar that’s filled.
- [var trackTintColor: UIColor?](./uiprogressview/tracktintcolor.md)
  The color shown for the portion of the progress bar that isn’t filled.
- [var trackImage: UIImage?](./uiprogressview/trackimage.md)
  An image to use for the portion of the track that isn’t filled.
### Constants
- [UIProgressView.Style](./uiprogressview/style.md)
  The styles permitted for the progress bar.

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
- [class UIActivityIndicatorView](./uiactivityindicatorview.md)
  A view that shows that a task is in progress.
- [class UICalendarView](./uicalendarview.md)
  A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [class UIContentUnavailableView](./uicontentunavailableview.md)
  A view that indicates there’s no content to display.
- [class UIImageView](./uiimageview.md)
  A view that displays a single image or a sequence of animated images in your interface.
- [class UIPickerView](./uipickerview.md)
  A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview)*