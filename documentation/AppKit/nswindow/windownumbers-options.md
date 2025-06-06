# windowNumbers(options:)

**Framework**: AppKit  
**Kind**: method

Returns the window numbers for all visible windows satisfying the specified options.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
class func windowNumbers(options: NSWindow.NumberListOptions = []) -> [NSNumber]?
```

#### Return Value

An array of window numbers for all visible windows satisfying the specified options. (Windows on the active space are returned in z-order; that is, front to back.)

## Parameters

- `options`: The possible options are specified in  .

## See Also

- [var depthLimit: NSWindow.Depth](nswindow/depthlimit.md)
  The depth limit of the window.
- [var hasDynamicDepthLimit: Bool](nswindow/hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [class var defaultDepthLimit: NSWindow.Depth](nswindow/defaultdepthlimit.md)
  Returns the default depth limit for instances of `NSWindow`.
- [var windowNumber: Int](nswindow/windownumber.md)
  The window number of the window’s window device.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](nswindow/devicedescription.md)
  A dictionary containing information about the window’s resolution, such as color, depth, and so on.
- [struct NSDeviceDescriptionKey](nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var canBecomeVisibleWithoutLogin: Bool](nswindow/canbecomevisiblewithoutlogin.md)
  A Boolean value that indicates whether the window can be displayed at the login window.
- [var sharingType: NSWindow.SharingType](nswindow/sharingtype-swift.property.md)
  A Boolean value that indicates the level of access other processes have to the window’s content.
- [var backingType: NSWindow.BackingStoreType](nswindow/backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nswindow/displaylink(target:selector:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/windownumbers(options:))*