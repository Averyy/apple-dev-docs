# colorSyncProfile

**Framework**: AppKit  
**Kind**: property

The ColorSync profile from which the color space was created.

**Availability**:
- macOS ?+

## Declaration

```swift
var colorSyncProfile: UnsafeMutableRawPointer? { get }
```

#### Discussion

The ColorSync profile on which the receiver is based. You need to cast this value to an object of opaque type CMProfileRef. Returns `NULL` if the receiver was created from a ICC-profile data instead. See [`ColorSync Manager`](https://developer.apple.com/documentation/applicationservices/colorsync_manager) for further information on CMProfileRef.

## See Also

- [var cgColorSpace: CGColorSpace?](nscolorspace/cgcolorspace.md)
  The Core Graphics color-space object that represents a color space equivalent to the color space’s.
- [var colorSpaceModel: NSColorSpace.Model](nscolorspace/colorspacemodel.md)
  The model on which the color space is based.
- [NSColorSpace.Model](nscolorspace/model.md)
  Constants that describe the abstract model on which color space objects are based.
- [var iccProfileData: Data?](nscolorspace/iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [var localizedName: String?](nscolorspace/localizedname.md)
  The localized name of the color space.
- [var numberOfColorComponents: Int](nscolorspace/numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/colorsyncprofile)*