# hasDynamicDepthLimit

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasDynamicDepthLimit: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window has a dynamic depth limit; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). When the value of [`hasDynamicDepthLimit`](nswindow/hasdynamicdepthlimit.md) is [`false`](https://developer.apple.com/documentation/Swift/false), the window uses either its preset depth limit or the default depth limit. A different, and non-dynamic, depth limit can be set using the [`depthLimit`](nswindow/depthlimit.md) property.

## See Also

- [var depthLimit: NSWindow.Depth](nswindow/depthlimit.md)
  The depth limit of the window.
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
- [var backingType: NSWindow.BackingStoreType](nswindow/backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nswindow/displaylink(target:selector:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/hasdynamicdepthlimit)*