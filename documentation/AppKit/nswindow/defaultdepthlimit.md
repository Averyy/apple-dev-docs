# defaultDepthLimit

**Framework**: AppKit  
**Kind**: property

Returns the default depth limit for instances of `NSWindow`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var defaultDepthLimit: NSWindow.Depth { get }
```

#### Return Value

The default depth limit for instances of `NSWindow`, determined by the depth of the deepest screen level available to the window server.

#### Discussion

The value returned can be examined with the Application Kit functions [`isPlanar`](nswindow/depth/isplanar.md), [`colorSpaceName`](nswindow/depth/colorspacename.md), [`bitsPerSample`](nswindow/depth/bitspersample.md), and [`bitsPerPixel`](nswindow/depth/bitsperpixel.md).

## See Also

- [func canStoreColor() -> Bool](nswindow/canstorecolor.md)
  Indicates whether the window has a depth limit that allows it to store color values.
- [var depthLimit: NSWindow.Depth](nswindow/depthlimit.md)
  The depth limit of the window.
- [var hasDynamicDepthLimit: Bool](nswindow/hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/defaultdepthlimit)*