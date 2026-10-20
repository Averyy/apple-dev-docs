# sharingType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the level of access other processes have to the window’s content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var sharingType: NSWindow.SharingType { get set }
```

```objc
@property NSWindowSharingType sharingType;
```

#### Discussion

The value of this property represents the sharing level of the window’s content. See [`NSWindow.SharingType`](./sharingtype-swift.enum.md) for possible values.

## See Also

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
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](./devicedescription.md)
  A dictionary containing information about the window’s resolution, such as color, depth, and so on.
- [struct NSDeviceDescriptionKey](../nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var canBecomeVisibleWithoutLogin: Bool](./canbecomevisiblewithoutlogin.md)
  A Boolean value that indicates whether the window can be displayed at the login window.
- [var backingType: NSWindow.BackingStoreType](./backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](./displaylink%28target,selector%29.md)
  Returns a new display link whose callback will be invoked in-sync with the display the window is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sharingtype-swift.property)*