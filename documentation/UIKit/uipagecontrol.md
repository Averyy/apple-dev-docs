# UIPageControl

**Framework**: UIKit  
**Kind**: class

A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPageControl
```

## Mentions

- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)
- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)

#### Overview

For an example of a page control, see the Weather app when it’s configured to display information for more than one location.

When a user taps a page control to move to the next or previous page, the control sends the [`valueChanged`](uicontrol/event/valuechanged.md) event for handling by the delegate. The delegate can then evaluate the [`currentPage`](uipagecontrol/currentpage.md) property to determine the page to display. The page control advances only one page in either direction. The currently viewed page is indicated by a white dot. Depending on the device, a certain number of dots are displayed on the screen before they’re clipped.

## Topics

### Managing pages
- [var currentPage: Int](uipagecontrol/currentpage.md)
  The current page, shown by the page control as a white dot.
- [var numberOfPages: Int](uipagecontrol/numberofpages.md)
  The number of pages the receiver shows (as dots).
- [var hidesForSinglePage: Bool](uipagecontrol/hidesforsinglepage.md)
  A Boolean value that controls whether the page control is hidden when there is only one page.
- [var defersCurrentPageDisplay: Bool](uipagecontrol/deferscurrentpagedisplay.md)
  A Boolean value that controls when the current page is displayed.
- [func updateCurrentPageDisplay()](uipagecontrol/updatecurrentpagedisplay.md)
  Updates the page indicator to the current page.
### Coloring the page indicator
- [var pageIndicatorTintColor: UIColor?](uipagecontrol/pageindicatortintcolor.md)
  The tint color to apply to the page indicator.
- [var currentPageIndicatorTintColor: UIColor?](uipagecontrol/currentpageindicatortintcolor.md)
  The tint color to apply to the current page indicator.
### Managing the indicator images
- [var preferredIndicatorImage: UIImage?](uipagecontrol/preferredindicatorimage.md)
  The preferred image for indicators.
- [func indicatorImage(forPage: Int) -> UIImage?](uipagecontrol/indicatorimage(forpage:).md)
  Returns the override image for the indicator of the specified page.
- [func setIndicatorImage(UIImage?, forPage: Int)](uipagecontrol/setindicatorimage(_:forpage:).md)
  Registers an override image for the indicator of the specified page.
- [var preferredCurrentPageIndicatorImage: UIImage?](uipagecontrol/preferredcurrentpageindicatorimage.md)
  The preferred image for the current page indicator.
- [func currentPageIndicatorImage(forPage: Int) -> UIImage?](uipagecontrol/currentpageindicatorimage(forpage:).md)
  Returns the override image for the current page indicator of the specified page.
- [func setCurrentPageIndicatorImage(UIImage?, forPage: Int)](uipagecontrol/setcurrentpageindicatorimage(_:forpage:).md)
  Registers an override image for the current page indicator of the specified page.
### Customizing the layout direction
- [var direction: UIPageControl.Direction](uipagecontrol/direction-swift.property.md)
  The layout direction of the page indicators.
- [UIPageControl.Direction](uipagecontrol/direction-swift.enum.md)
  Decribes the layout direction of a page control’s indicators.
### Customizing the background style
- [var backgroundStyle: UIPageControl.BackgroundStyle](uipagecontrol/backgroundstyle-swift.property.md)
  The preferred background style.
- [UIPageControl.BackgroundStyle](uipagecontrol/backgroundstyle-swift.enum.md)
  Constants that define the background styles of the page control.
### Customizing the interaction state
- [var allowsContinuousInteraction: Bool](uipagecontrol/allowscontinuousinteraction.md)
  A Boolean value that determines whether the page control allows continuous interaction.
- [var interactionState: UIPageControl.InteractionState](uipagecontrol/interactionstate-swift.property.md)
  The interaction state when the current page changes.
- [UIPageControl.InteractionState](uipagecontrol/interactionstate-swift.enum.md)
  Constants that define the interaction states of the page control.
### Calculating the control size
- [func size(forNumberOfPages: Int) -> CGSize](uipagecontrol/size(fornumberofpages:).md)
  Returns the size the receiver’s bounds should be to accommodate the given number of pages.
### Configuring page progress
- [var progress: UIPageControlProgress?](uipagecontrol/progress.md)
- [class UIPageControlProgress](uipagecontrolprogress.md)
- [class UIPageControlTimerProgress](uipagecontroltimerprogress.md)
- [protocol UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)
- [protocol UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
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

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class UIControl](uicontrol.md)
  The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
- [class UIButton](uibutton.md)
  A control that executes your custom code in response to user interactions.
- [class UIColorWell](uicolorwell.md)
  A control that displays a color picker.
- [class UIDatePicker](uidatepicker.md)
  A control for inputting date and time values.
- [class UISegmentedControl](uisegmentedcontrol.md)
  A horizontal control that consists of multiple segments, each segment functioning as a discrete button.
- [class UISlider](uislider.md)
  A control for selecting a single value from a continuous range of values.
- [class UIStepper](uistepper.md)
  A control for incrementing or decrementing a value.
- [class UISwitch](uiswitch.md)
  A control that offers a binary choice, such as on/off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol)*