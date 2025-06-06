# backingType

**Framework**: AppKit  
**Kind**: property

The window’s backing store type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var backingType: NSWindow.BackingStoreType { get set }
```

#### Discussion

The possible values for this property are described in [`NSWindow.BackingStoreType`](nswindow/backingstoretype.md). You can set the property only to switch a buffered window to retained or vice versa; you can’t change the backing type to or from nonretained after initializing a `NSWindow` object (an error is generated if you attempt to do so).

## See Also

- [convenience init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool, screen: NSScreen?)](nswindow/init(contentrect:stylemask:backing:defer:screen:).md)
  Initializes an allocated window with the specified values.
- [init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool)](nswindow/init(contentrect:stylemask:backing:defer:).md)
  Initializes the window with the specified values.
- [var depthLimit: NSWindow.Depth](nswindow/depthlimit.md)
  The depth limit of the window.
- [var hasDynamicDepthLimit: Bool](nswindow/hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [class var defaultDepthLimit: NSWindow.Depth](nswindow/defaultdepthlimit.md)
  Returns the default depth limit for instances of `NSWindow`.
- [var windowNumber: Int](nswindow/windownumber.md)
  The window number of the window’s window device.
- [class func windowNumbers(options: NSWindow.NumberListOptions) -> [NSNumber]?](nswindow/windownumbers(options:).md)
  Returns the window numbers for all visible windows satisfying the specified options.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](nswindow/devicedescription.md)
  A dictionary containing information about the window’s resolution, such as color, depth, and so on.
- [struct NSDeviceDescriptionKey](nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var canBecomeVisibleWithoutLogin: Bool](nswindow/canbecomevisiblewithoutlogin.md)
  A Boolean value that indicates whether the window can be displayed at the login window.
- [var sharingType: NSWindow.SharingType](nswindow/sharingtype-swift.property.md)
  A Boolean value that indicates the level of access other processes have to the window’s content.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nswindow/displaylink(target:selector:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingtype)*