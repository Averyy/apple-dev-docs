# canBecomeVisibleWithoutLogin

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window can be displayed at the login window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var canBecomeVisibleWithoutLogin: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window can be displayed at the login window; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). By default, the value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

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
- [var sharingType: NSWindow.SharingType](nswindow/sharingtype-swift.property.md)
  A Boolean value that indicates the level of access other processes have to the window’s content.
- [var backingType: NSWindow.BackingStoreType](nswindow/backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nswindow/displaylink(target:selector:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/canbecomevisiblewithoutlogin)*