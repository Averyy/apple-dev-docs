# deviceDescription

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A dictionary containing information about the window’s resolution, such as color, depth, and so on.

**Availability**:
- macOS

## Declaration

```swift
var deviceDescription: [NSDeviceDescriptionKey : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * deviceDescription;
```

#### Discussion

This information is useful for tuning images and colors to the window’s display capabilities. The contents of the dictionary are described in `Display Device—Descriptions`.

## See Also

### Related Documentation
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](../nscolor/usingcolorspacename%28_%29.md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](../nsscreen/devicedescription.md)
  The device dictionary for the screen.
### Accessing Window Information
- [var depthLimit: NSWindow.Depth](./depthlimit.md)
  The depth limit of the window.
- [var hasDynamicDepthLimit: Bool](./hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [class var defaultDepthLimit: NSWindow.Depth](./defaultdepthlimit.md)
  Returns the default depth limit for instances of `NSWindow`.
- [var windowNumber: Int](./windownumber.md)
  The window number of the window’s window device.
- [class func windowNumbers(options: NSWindow.NumberListOptions) -> [NSNumber]?](./windownumbers%28options%29.md)
  Returns the window numbers for all visible windows satisfying the specified options.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/devicedescription)*