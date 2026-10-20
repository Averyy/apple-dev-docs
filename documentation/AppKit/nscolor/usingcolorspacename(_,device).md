# usingColorSpaceName(_:device:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new color object for the same color, but in the specified color space and specific to the provided device.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use -colorUsingType: or -colorUsingColorSpace: instead

## Declaration

```swift
func usingColorSpaceName(_ name: NSColorSpaceName?, device deviceDescription: [NSDeviceDescriptionKey : Any]?) -> NSColor?
```

```objc
- (NSColor *) colorUsingColorSpaceName:(NSColorSpaceName) name device:(NSDictionary<NSString *,id> *) deviceDescription;
```

#### Return Value

The new NSColor object or `nil` if the specified conversion cannot be done.

## Parameters

- `name`: The name of the color space containing the new `NSColor` object. If `colorSpace` is `nil`, the most appropriate color space is used.
- `deviceDescription`: The device description. Device descriptions can be obtained from windows, screens, and printers with the `deviceDescription` method.

  If `deviceDescription` is `nil`, the current device (as obtained from the currently lockFocus’ed view’s window or, if printing, the current printer) is used.

## See Also

### Related Documentation
- [var colorSpaceName: NSColorSpaceName](./colorspacename.md)
  The name of the color space associated with the color.
### Deprecated methods
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](./usingcolorspacename%28_%29.md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/usingcolorspacename(_:device:))*