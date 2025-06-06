# NSScreen

**Framework**: Appkit  
**Kind**: class

An object that describes the attributes of a computer’s monitor or screen.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSScreen
```

#### Overview

An app may use an [`NSScreen`](nsscreen.md) object to retrieve information about a screen and use this information to decide what to display on that screen. For example, an app may use the [`deepest`](nsscreen/deepest.md) method to find out which of the available screens can best represent color and then might choose to display all of its windows on that screen.

Create the application object before you use the methods in this class, so that the application object can make the necessary connection to the window system. You can make sure the application object exists by invoking the [`shared`](nsapplication/shared.md) method of [`NSApplication`](nsapplication.md). If you created your app with Xcode, the application object is automatically created for you during initialization.

> **Note**:  The [`NSScreen`](nsscreen.md) class is only for getting information about the available displays. If you need additional information or want to change the attributes relating to a display, you must use Quartz Services. For more information, see [`Quartz Display Services`](https://developer.apple.com/documentation/CoreGraphics/quartz-display-services).

## Topics

### Getting Screen Objects
- [class var main: NSScreen?](nsscreen/main.md)
  Returns the screen object containing the window with the keyboard focus.
- [class var deepest: NSScreen?](nsscreen/deepest.md)
  Returns a screen object representing the screen that can best represent color.
- [class var screens: [NSScreen]](nsscreen/screens.md)
  Returns an array of screen objects representing all of the screens available on the system.
### Getting Screen Information
- [var depth: NSWindow.Depth](nsscreen/depth.md)
  The current bit depth and colorspace information of the screen.
- [var frame: NSRect](nsscreen/frame.md)
  The dimensions and location of the screen.
- [var supportedWindowDepths: UnsafePointer<NSWindow.Depth>](nsscreen/supportedwindowdepths.md)
  A zero-terminated array of the window depths supported by the screen.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](nsscreen/devicedescription.md)
  The device dictionary for the screen.
- [struct NSDeviceDescriptionKey](nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var colorSpace: NSColorSpace?](nsscreen/colorspace.md)
  The color space of the screen.
- [var localizedName: String](nsscreen/localizedname.md)
  The localized name of the display.
- [func canRepresent(NSDisplayGamut) -> Bool](nsscreen/canrepresent(_:).md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](nsdisplaygamut.md)
- [class var screensHaveSeparateSpaces: Bool](nsscreen/screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.
### Converting Between Screen and Backing Coordinates
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](nsscreen/backingalignedrect(_:options:).md)
  Converts a rectangle in global screen coordinates to a pixel aligned rectangle.
- [var backingScaleFactor: CGFloat](nsscreen/backingscalefactor.md)
  The backing store pixel scale factor for the screen.
- [func convertRectFromBacking(NSRect) -> NSRect](nsscreen/convertrectfrombacking(_:).md)
  Converts the rectangle from the device pixel aligned coordinates system of a screen.
- [func convertRectToBacking(NSRect) -> NSRect](nsscreen/convertrecttobacking(_:).md)
  Converts the rectangle to the device pixel aligned coordinates system of a screen.
### Getting the Visible Portion of the Screen
- [var visibleFrame: NSRect](nsscreen/visibleframe.md)
  The current location and dimensions of the visible screen.
- [var safeAreaInsets: NSEdgeInsets](nsscreen/safeareainsets.md)
  The distances from the screen’s edges at which content isn’t obscured.
- [var auxiliaryTopLeftArea: NSRect?](nsscreen/auxiliarytopleftarea-uglc.md)
  The unobscured portion of the top-left corner of the screen.
- [var auxiliaryTopRightArea: NSRect?](nsscreen/auxiliarytoprightarea-gr2n.md)
  The unobscured portion of the top-right corner of the screen.
### Getting Extended Dynamic Range Details
- [var maximumPotentialExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumpotentialextendeddynamicrangecolorcomponentvalue.md)
  The maximum possible color component value for the screen when it’s in extended dynamic range (EDR) mode.
- [var maximumExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for the screen.
- [var maximumReferenceExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumreferenceextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for reference rendering to the screen.
### Getting Variable Refresh Rate Details
- [var maximumFramesPerSecond: Int](nsscreen/maximumframespersecond.md)
  The maximum number of frames per second that the screen supports.
- [var minimumRefreshInterval: TimeInterval](nsscreen/minimumrefreshinterval.md)
  The shortest refresh interval that the screen supports.
- [var maximumRefreshInterval: TimeInterval](nsscreen/maximumrefreshinterval.md)
  The largest refresh interval that the screen supports.
- [var displayUpdateGranularity: TimeInterval](nsscreen/displayupdategranularity.md)
  The number of seconds between the screen’s supported update rates, for screens that support fixed update rates.
- [var lastDisplayUpdateTimestamp: TimeInterval](nsscreen/lastdisplayupdatetimestamp.md)
  The time of the last framebuffer update, expressed as the number of seconds since system startup.
### Receiving Screen-Related Notifications
- [class let colorSpaceDidChangeNotification: NSNotification.Name](nsscreen/colorspacedidchangenotification.md)
  Posted when the color space of the screen has changed.
### Synchronizing with the display’s refresh rate
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nsscreen/displaylink(target:selector:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsscreen)*