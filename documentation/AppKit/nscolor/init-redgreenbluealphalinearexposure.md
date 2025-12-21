# init(red:green:blue:alpha:linearExposure:)

**Framework**: AppKit  
**Kind**: init

Generates an HDR color in the extended sRGB colorspace by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value >= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.

**Availability**:
- macOS 26.0+

## Declaration

```swift
init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, linearExposure: CGFloat)
```

## See Also

- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)](nscolor/init(red:green:blue:alpha:exposure:).md)
  Generates an HDR color in the extended sRGB colorspace by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value >= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(red:green:blue:alpha:linearexposure:))*