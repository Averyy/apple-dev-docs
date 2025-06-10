# NSTitlebarAccessoryViewController

**Framework**: AppKit  
**Kind**: class

An object that manages a custom view—known as an accessory view—in the title bar–toolbar area of a window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSTitlebarAccessoryViewController
```

#### Overview

Because a title bar accessory view controller is contained in a visual effect view (that is, [`NSVisualEffectView`](nsvisualeffectview.md)), it automatically handles the blur behind the accessory view and the size and location changes for the content of the view when a window goes in and out of full screen mode. If you’re currently using [`NSToolbar`](nstoolbar.md) fullscreen accessory APIs, such as [`fullScreenAccessoryView`](nstoolbar/fullscreenaccessoryview.md), you should use [`NSTitlebarAccessoryViewController`](nstitlebaraccessoryviewcontroller.md) APIs instead.

Typically, you create an `NSTitlebarAccessoryViewController` object, give it your custom view, set the [`layoutAttribute`](nstitlebaraccessoryviewcontroller/layoutattribute.md) property to ensure that it displays correctly in relation to the title bar, and add the view controller to your window. For more information about [`NSWindow`](nswindow.md) methods you can use to add and remove a title bar accessory view controller, see Managing Title Bars.

Don’t override the `view` property in your `NSTitlebarAccessoryViewController` subclass. Instead, you can override [`loadView()`](nsviewcontroller/loadview().md), and set the `view` property in that method.

> **Note**:  `NSTitlebarAccessoryViewController` observes the view’s frame for changes. Depending on the value of [`layoutAttribute`](nstitlebaraccessoryviewcontroller/layoutattribute.md), you can change either the height or the width of the view. Specifically, you can change the view’s height when [`layoutAttribute`](nstitlebaraccessoryviewcontroller/layoutattribute.md) is [`NSLayoutConstraint.Attribute.bottom`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/bottom), and you can change the view’s width when the [`layoutAttribute`](nstitlebaraccessoryviewcontroller/layoutattribute.md) is [`NSLayoutConstraint.Attribute.right`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/right) or [`NSLayoutConstraint.Attribute.left`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/left). The remaining size direction is automatically set to the maximum size as required for the window.

## Topics

### Configuring a Title Bar Accessory View Controller
- [var fullScreenMinHeight: CGFloat](nstitlebaraccessoryviewcontroller/fullscreenminheight.md)
  The visual minimum height of an accessory view that displays below the title bar when the window is in full screen mode.
- [var layoutAttribute: NSLayoutConstraint.Attribute](nstitlebaraccessoryviewcontroller/layoutattribute.md)
  The location of the accessory view, in relation to the window’s title bar.
### Responding to View Events
- [func viewDidAppear()](nstitlebaraccessoryviewcontroller/viewdidappear.md)
  Called when the title bar accessory view controller’s view is fully transitioned onto the screen.
- [func viewDidDisappear()](nstitlebaraccessoryviewcontroller/viewdiddisappear.md)
  Called after the title bar accessory view controller’s view is removed from the window’s view hierarchy.
- [func viewWillAppear()](nstitlebaraccessoryviewcontroller/viewwillappear.md)
  Called after the title bar accessory view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.
### Instance Properties
- [var automaticallyAdjustsSize: Bool](nstitlebaraccessoryviewcontroller/automaticallyadjustssize.md)
- [var isHidden: Bool](nstitlebaraccessoryviewcontroller/ishidden.md)

## Relationships

### Inherits From
- [NSViewController](nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAnimationDelegate](nsanimationdelegate.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](nssegueperforming.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSWindowController](nswindowcontroller.md)
  A controller that manages a window, usually a window stored in a nib file.
- [class NSViewController](nsviewcontroller.md)
  A controller that manages a view, typically loaded from a nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller)*