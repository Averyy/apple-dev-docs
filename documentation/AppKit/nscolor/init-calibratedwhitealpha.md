# init(calibratedWhite:alpha:)

**Framework**: AppKit  
**Kind**: init

Creates a color object using the given opacity and grayscale values.

**Availability**:
- macOS ?+

## Declaration

```swift
init(calibratedWhite white: CGFloat, alpha: CGFloat)
```

#### Return Value

The color object.

#### Discussion

Values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## Parameters

- `white`: The grayscale value of the color object.
- `alpha`: The opacity value of the color object.

## See Also

- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getwhite(_:alpha:).md)
  Returns the grayscale and alpha values of the color.
- [init(white: CGFloat, alpha: CGFloat)](nscolor/init(white:alpha:).md)
  Creates a color object with the specified brightness and alpha channel values.
- [init(deviceWhite: CGFloat, alpha: CGFloat)](nscolor/init(devicewhite:alpha:).md)
  Creates a color object using the given opacity and grayscale values.
- [init(genericGamma22White: CGFloat, alpha: CGFloat)](nscolor/init(genericgamma22white:alpha:).md)
  Returns a color object with the specified white and alpha values in the GenericGamma22 colorspace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(calibratedwhite:alpha:))*