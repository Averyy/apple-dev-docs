# backingType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window’s backing store type.

**Availability**:
- macOS

## Declaration

```swift
var backingType: NSWindow.BackingStoreType { get set }
```

```objc
@property NSBackingStoreType backingType;
```

## Discussion

The possible values for this property are described in [`NSWindow.BackingStoreType`](./backingstoretype.md). You can set the property only to switch a buffered window to retained or vice versa; you can’t change the backing type to or from nonretained after initializing a `NSWindow` object (an error is generated if you attempt to do so).

## See Also

### Related Documentation
- [convenience init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool, screen: NSScreen?)](./init%28contentrect,stylemask,backing,defer,screen%29.md)
  Initializes an allocated window with the specified values.
- [init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool)](./init%28contentrect,stylemask,backing,defer%29.md)
  Initializes the window with the specified values.
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
- [var sharingType: NSWindow.SharingType](./sharingtype-swift.property.md)
  A Boolean value that indicates the level of access other processes have to the window’s content.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](./displaylink%28target,selector%29.md)
  Returns a new display link whose callback will be invoked in-sync with the display the window is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingtype)*