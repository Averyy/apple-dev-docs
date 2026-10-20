# defaultDepthLimit

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default depth limit for instances of `NSWindow`.

**Availability**:
- macOS

## Declaration

```swift
class var defaultDepthLimit: NSWindow.Depth { get }
```

```objc
@property (class, readonly) NSWindowDepth defaultDepthLimit;
```

#### Return Value

The default depth limit for instances of `NSWindow`, determined by the depth of the deepest screen level available to the window server.

#### Discussion

The value returned can be examined with the Application Kit functions [`isPlanar`](./depth/isplanar.md), [`colorSpaceName`](./depth/colorspacename.md), [`bitsPerSample`](./depth/bitspersample.md), and [`bitsPerPixel`](./depth/bitsperpixel.md).

## See Also

### Related Documentation
- [func canStoreColor() -> Bool](./canstorecolor%28%29.md)
  Indicates whether the window has a depth limit that allows it to store color values.
### Accessing Window Information
- [var depthLimit: NSWindow.Depth](./depthlimit.md)
  The depth limit of the window.
- [var hasDynamicDepthLimit: Bool](./hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/defaultdepthlimit)*