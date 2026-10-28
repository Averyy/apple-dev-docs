# usingColorSpaceName(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use -colorUsingType: or -colorUsingColorSpace: instead

## Declaration

```swift
func usingColorSpaceName(_ name: NSColorSpaceName) -> NSColor?
```

```objc
- (NSColor *) colorUsingColorSpaceName:(NSColorSpaceName) name;
```

## Return Value

The new `NSColor` object or `nil` if the specified conversion cannot be done.

## Parameters

- `name`: The name of the color space containing the new `NSColor` object.

## See Also

### Related Documentation
- [var colorSpaceName: NSColorSpaceName](./colorspacename.md)
  The name of the color space associated with the color.
### Deprecated methods
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](./usingcolorspacename%28_,device%29.md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/usingcolorspacename(_:))*