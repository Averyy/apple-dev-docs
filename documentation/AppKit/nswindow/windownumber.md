# windowNumber

**Framework**: AppKit  
**Kind**: property

The window number of the window’s window device.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windowNumber: Int { get }
```

#### Discussion

Each window device in an application is given a unique window number—note that this isn’t the same as the global window number assigned by the window server. This number can be used to identify the window device with the [`order(_:relativeTo:)`](nswindow/order(_:relativeto:).md) method and in the AppKit function [`NSWindowList`](nswindowlist.md).

If the window doesn’t have a window device, the value of this property is equal to or less than `0`.

## See Also

- [var isOneShot: Bool](nswindow/isoneshot.md)
  A Boolean value that indicates whether the window device the window manages is freed when it’s removed from the screen list.
- [init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool)](nswindow/init(contentrect:stylemask:backing:defer:).md)
  Initializes the window with the specified values.
- [var depthLimit: NSWindow.Depth](nswindow/depthlimit.md)
  The depth limit of the window.
- [var hasDynamicDepthLimit: Bool](nswindow/hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [class var defaultDepthLimit: NSWindow.Depth](nswindow/defaultdepthlimit.md)
  Returns the default depth limit for instances of `NSWindow`.
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
- [var backingType: NSWindow.BackingStoreType](nswindow/backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nswindow/displaylink(target:selector:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/windownumber)*