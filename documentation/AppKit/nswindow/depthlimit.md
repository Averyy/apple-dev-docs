# depthLimit

**Framework**: AppKit  
**Kind**: property

The depth limit of the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var depthLimit: NSWindow.Depth { get set }
```

#### Discussion

The value of this property can be examined with the Application Kit functions [`isPlanar`](nswindow/depth/isplanar.md), [`colorSpaceName`](nswindow/depth/colorspacename.md), [`bitsPerSample`](nswindow/depth/bitspersample.md), and [`bitsPerPixel`](nswindow/depth/bitsperpixel.md). In addition, the [`NSBestDepth`](nsbestdepth.md) function provides the best depth limit based on a set of parameters.

Setting this property to `0` sets the depth limit to the window’s default depth limit. A depth limit of `0` can be useful for reverting a window object to its initial depth. You can also use one of the explicit bit depths defined in `Explicit Window Depth Limits` ([`NSWindow.Depth.twentyfourBitRGB`](nswindow/depth/twentyfourbitrgb.md) is the default).

## See Also

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
- [var backingType: NSWindow.BackingStoreType](nswindow/backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nswindow/displaylink(target:selector:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depthlimit)*