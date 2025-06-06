# init(colorSpace:components:count:)

**Framework**: AppKit  
**Kind**: init

Creates a color object from the specified components of the given color space.

**Availability**:
- macOS ?+

## Declaration

```swift
init(colorSpace space: NSColorSpace, components: UnsafePointer<CGFloat>, count numberOfComponents: Int)
```

#### Return Value

The color object.

## Parameters

- `space`: An   object representing a color space. The colorspace should be component-based. The method raises if this is   or a color space that cannot be used with   objects.
- `components`: An array of the components in the specified color space to use to create the   object. The order of these components is determined by the color-space profile, with the alpha component always last. (If you want the created color to be opaque, specify 1.0 for the alpha component.)
- `numberOfComponents`: The number of components in the   array. This should match the number dictated by the specified color space plus one for alpha. This method raises an exception if they do not match.

## See Also

- [func usingColorSpace(NSColorSpace) -> NSColor?](nscolor/usingcolorspace(_:).md)
  Creates a new color object representing the color of the current color object in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(colorspace:components:count:))*