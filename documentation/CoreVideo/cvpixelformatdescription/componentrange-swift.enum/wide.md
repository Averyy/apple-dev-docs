# CVPixelFormatDescription.ComponentRange.wide

**Framework**: Core Video  
**Kind**: case

Indicates that this component represents the nominal range of values in a color component using a dramatically reduced range of integer values, in order to allow expression of values broadly outside the normal -1.0 to 1.0 and/or 0.0 to 1.0 ranges.  For example, formats supporting Extended sRGB allow component values that are less than 0.0 or greater than 1.0 in order to depict colors outside the sRGB colorimetry.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
case wide
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/componentrange-swift.enum/wide)*