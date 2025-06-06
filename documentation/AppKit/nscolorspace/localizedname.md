# localizedName

**Framework**: AppKit  
**Kind**: property

The localized name of the color space.

**Availability**:
- macOS ?+

## Declaration

```swift
var localizedName: String? { get }
```

#### Discussion

This property holds the name of the color space as a localized string or `nil` if no localized name exists.

## See Also

- [var cgColorSpace: CGColorSpace?](nscolorspace/cgcolorspace.md)
  The Core Graphics color-space object that represents a color space equivalent to the color space’s.
- [var colorSpaceModel: NSColorSpace.Model](nscolorspace/colorspacemodel.md)
  The model on which the color space is based.
- [NSColorSpace.Model](nscolorspace/model.md)
  Constants that describe the abstract model on which color space objects are based.
- [var colorSyncProfile: UnsafeMutableRawPointer?](nscolorspace/colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
- [var iccProfileData: Data?](nscolorspace/iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [var numberOfColorComponents: Int](nscolorspace/numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/localizedname)*