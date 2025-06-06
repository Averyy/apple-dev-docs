# ScreenSaverView

**Framework**: Screensaver  
**Kind**: class

An abstract class that defines the interface for subclassers to interact with the screen saver infrastructure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class ScreenSaverView
```

#### Overview

[`ScreenSaverView`](screensaverview.md) provides the interface for your screen saver, including the content you animate onscreen and an optional configuration sheet. Create your own custom subclass and add it to your screen saver bundle. Use your subclass to create the animations that you want to appear onscreen, and to specify additional animation details.

> **Note**:  When someone previews your screen saver in System Preferences, the system instantiates your [`ScreenSaverView`](screensaverview.md) subclass.

You can draw from your view’s [`draw(_:)`](screensaverview/draw(_:).md) method, or you can draw directly from the [`animateOneFrame()`](screensaverview/animateoneframe().md) method. If you prefer to use the [`draw(_:)`](screensaverview/draw(_:).md) method, use the [`animateOneFrame()`](screensaverview/animateoneframe().md) method to call the [`setNeedsDisplay(_:)`](https://developer.apple.com/documentation/AppKit/NSView/setNeedsDisplay(_:)) method and specify the portions of your view that require updates.

## Topics

### Creating a screen saver view
- [init?(frame: NSRect, isPreview: Bool)](screensaverview/init(frame:ispreview:).md)
  Creates a newly allocated screen saver view with the specified frame rectangle and preview information.
### Getting the preferred window behavior
- [class func backingStoreType() -> NSWindow.BackingStoreType](screensaverview/backingstoretype.md)
  Returns the type of backing store you want for your screen saver’s window.
- [class func performGammaFade() -> Bool](screensaverview/performgammafade.md)
  Indicates whether to perform a gradual screen fade when the system starts and stops your screen saver’s animation.
### Setting and getting the animation time interval
- [var animationTimeInterval: TimeInterval](screensaverview/animationtimeinterval.md)
  The time interval between animation frames.
### Animating the screen saver
- [func startAnimation()](screensaverview/startanimation.md)
  Activates the periodic timer that animates the screen saver.
- [func animateOneFrame()](screensaverview/animateoneframe.md)
  Advances the screen saver’s animation by a single frame.
- [func stopAnimation()](screensaverview/stopanimation.md)
  Deactivates the timer that advances the animation.
- [var isAnimating: Bool](screensaverview/isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.
### Drawing the view
- [func draw(NSRect)](screensaverview/draw(_:).md)
  Draws the screen saver view.
- [var isPreview: Bool](screensaverview/ispreview.md)
  A Boolean value that indicates whether the screen saver view is set to a size suitable for previewing its content.
### Accessing the configuration sheet
- [var hasConfigureSheet: Bool](screensaverview/hasconfiguresheet.md)
  A Boolean value that indicates whether the screen saver has an associated configuration sheet.
- [var configureSheet: NSWindow?](screensaverview/configuresheet.md)
  The window that contains the controls to configure the screen saver.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)

## See Also

- [class ScreenSaverDefaults](screensaverdefaults.md)
  A class that defines a set of methods for saving and restoring user defaults for screen savers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ScreenSaver/screensaverview)*