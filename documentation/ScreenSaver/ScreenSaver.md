# Screen Saver

**Framework**: Screensaver  
**Kind**: module

Animate screen savers, and interact with the screen saver infrastructure.

**Availability**:
- macOS 10.0+

#### Overview

The Screen Saver framework defines the interface for custom modules to interact with the Screen Effects user interface feature. Write screen savers in Objective-C, and implement your module’s user interface using Cocoa. Use the available functions to produce random values and centering rectangles.

To create a screen saver, create a bundle directory with the `.saver` suffix and install it in one of the `Library/Screen Savers` directories on the system. In your bundle’s executable, include a [`ScreenSaverView`](screensaverview.md) subclass. That view defines the interface you use to generate your screen saver content. If your screen saver stores any preference information, use the [`ScreenSaverDefaults`](screensaverdefaults.md) class instead of the standard [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) class.

Because screen savers are plug-ins for the screen saver engine, the screen saver binary must support the same hardware architecture of the running engine. As with any application, the screen saver engine uses the native architecture of the host computer. For full compatibility, make sure your screen saver supports both the `x86_64` and `arm64` architectures.

##### How the System Runs Your Screen Saver

When macOS starts your screen saver, the system:

1. Fades the screen to black.
2. Instantiates your [`ScreenSaverView`](screensaverview.md) subclass and calls its [`init(frame:isPreview:)`](screensaverview/init(frame:ispreview:).md) method.
3. Creates a window and installs your [`ScreenSaverView`](screensaverview.md) subclass in it.
4. Activates the window and sets its order.
5. Calls your view’s [`draw(_:)`](screensaverview/draw(_:).md) method so you can draw your initial state.
6. Fades in the screen to reveal your window in the front.
7. Calls your view’s [`startAnimation()`](screensaverview/startanimation().md) method, which you use to set up any animation-related state information.
8. Calls your view’s [`animateOneFrame()`](screensaverview/animateoneframe().md) method repeatedly.

When the user takes some action, the system calls your view’s [`stopAnimation()`](screensaverview/stopanimation().md) method to stop your screen saver. Use that method to clean up any state information you establish in your [`startAnimation()`](screensaverview/startanimation().md) method.

> **Note**:  The [`stopAnimation()`](screensaverview/stopanimation().md) or [`startAnimation()`](screensaverview/startanimation().md) methods don’t immediately start or stop the animations. The system can still call your [`animateOneFrame()`](screensaverview/animateoneframe().md) method after calling [`stopAnimation()`](screensaverview/stopanimation().md).

## Topics

### Interface
- [class ScreenSaverView](screensaverview.md)
  An abstract class that defines the interface for subclassers to interact with the screen saver infrastructure.
- [class ScreenSaverDefaults](screensaverdefaults.md)
  A class that defines a set of methods for saving and restoring user defaults for screen savers.
### Utilities
- [func SSRandomIntBetween(Int32, Int32) -> Int32](ssrandomintbetween(_:_:).md)
  Returns a random integer value.
- [func SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat](ssrandomfloatbetween(_:_:).md)
  Returns a random float value.
- [func SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint](ssrandompointforsizewithinrect(_:_:).md)
  Returns a random point.
- [func SSCenteredRectInRect(NSRect, NSRect) -> NSRect](sscenteredrectinrect(_:_:).md)
  Returns a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ScreenSaver)*