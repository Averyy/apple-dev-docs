# ScreenSaverView

**Framework**: Screen Saver  
**Kind**: class  
**Role**: Class

An abstract class that defines the interface for subclassers to interact with the screen saver infrastructure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class ScreenSaverView
```

```objc
@interface ScreenSaverView : NSView
```

#### Overview

[`ScreenSaverView`](./screensaverview.md) provides the interface for your screen saver, including the content you animate onscreen and an optional configuration sheet. Create your own custom subclass and add it to your screen saver bundle. Use your subclass to create the animations that you want to appear onscreen, and to specify additional animation details.

> **Note**:  When someone previews your screen saver in System Preferences, the system instantiates your [`ScreenSaverView`](./screensaverview.md) subclass.

You can draw from your view’s [`draw(_:)`](./screensaverview/draw%28_%29.md) method, or you can draw directly from the [`animateOneFrame()`](./screensaverview/animateoneframe%28%29.md) method. If you prefer to use the [`draw(_:)`](./screensaverview/draw%28_%29.md) method, use the [`animateOneFrame()`](./screensaverview/animateoneframe%28%29.md) method to call the [`setNeedsDisplay(_:)`](../AppKit/nsview/setneedsdisplay%28_%29.md) method and specify the portions of your view that require updates.

## Topics

### Creating a screen saver view
- [init?(frame: NSRect, isPreview: Bool)](./screensaverview/init%28frame,ispreview%29.md)
  Creates a newly allocated screen saver view with the specified frame rectangle and preview information.
### Getting the preferred window behavior
- [class func backingStoreType() -> NSWindow.BackingStoreType](./screensaverview/backingstoretype%28%29.md)
  Returns the type of backing store you want for your screen saver’s window.
- [class func performGammaFade() -> Bool](./screensaverview/performgammafade%28%29.md)
  Indicates whether to perform a gradual screen fade when the system starts and stops your screen saver’s animation.
### Setting and getting the animation time interval
- [var animationTimeInterval: TimeInterval](./screensaverview/animationtimeinterval.md)
  The time interval between animation frames.
### Animating the screen saver
- [func startAnimation()](./screensaverview/startanimation%28%29.md)
  Activates the periodic timer that animates the screen saver.
- [func animateOneFrame()](./screensaverview/animateoneframe%28%29.md)
  Advances the screen saver’s animation by a single frame.
- [func stopAnimation()](./screensaverview/stopanimation%28%29.md)
  Deactivates the timer that advances the animation.
- [var isAnimating: Bool](./screensaverview/isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.
### Drawing the view
- [func draw(NSRect)](./screensaverview/draw%28_%29.md)
  Draws the screen saver view.
- [var isPreview: Bool](./screensaverview/ispreview.md)
  A Boolean value that indicates whether the screen saver view is set to a size suitable for previewing its content.
### Accessing the configuration sheet
- [var hasConfigureSheet: Bool](./screensaverview/hasconfiguresheet.md)
  A Boolean value that indicates whether the screen saver has an associated configuration sheet.
- [var configureSheet: NSWindow?](./screensaverview/configuresheet.md)
  The window that contains the controls to configure the screen saver.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)

## See Also

### Interface
- [class ScreenSaverDefaults](./screensaverdefaults.md)
  A class that defines a set of methods for saving and restoring user defaults for screen savers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview)*