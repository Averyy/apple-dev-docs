# depthLimit

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The depth limit of the window.

**Availability**:
- macOS

## Declaration

```swift
var depthLimit: NSWindow.Depth { get set }
```

```objc
@property NSWindowDepth depthLimit;
```

## Discussion

The value of this property can be examined with the Application Kit functions [`isPlanar`](./depth/isplanar.md), [`colorSpaceName`](./depth/colorspacename.md), [`bitsPerSample`](./depth/bitspersample.md), and [`bitsPerPixel`](./depth/bitsperpixel.md). In addition, the [`NSBestDepth`](../nsbestdepth.md) function provides the best depth limit based on a set of parameters.

Setting this property to `0` sets the depth limit to the window’s default depth limit. A depth limit of `0` can be useful for reverting a window object to its initial depth. You can also use one of the explicit bit depths defined in `Explicit Window Depth Limits` ([`NSWindow.Depth.twentyfourBitRGB`](./depth/twentyfourbitrgb.md) is the default).

## See Also

### Accessing Window Information
- [var hasDynamicDepthLimit: Bool](./hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [class var defaultDepthLimit: NSWindow.Depth](./defaultdepthlimit.md)
  Returns the default depth limit for instances of `NSWindow`.
- [var windowNumber: Int](./windownumber.md)
  The window number of the window’s window device.
- [class func windowNumbers(options: NSWindow.NumberListOptions) -> [NSNumber]?](./windownumbers%28options%29.md)
  Returns the window numbers for all visible windows satisfying the specified options.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](./devicedescription.md)
  A dictionary containing information about the window’s resolution, such as color, depth, and so on.
- [struct NSDeviceDescriptionKey](../nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var canBecomeVisibleWithoutLogin: Bool](./canbecomevisiblewithoutlogin.md)
  A Boolean value that indicates whether the window can be displayed at the login window.
- [var sharingType: NSWindow.SharingType](./sharingtype-swift.property.md)
  A Boolean value that indicates the level of access other processes have to the window’s content.
- [var backingType: NSWindow.BackingStoreType](./backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](./displaylink%28target,selector%29.md)
  Returns a new display link whose callback will be invoked in-sync with the display the window is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depthlimit)*