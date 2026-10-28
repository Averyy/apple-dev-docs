# colorSpaceModel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The model on which the color space is based.

**Availability**:
- macOS

## Declaration

```swift
var colorSpaceModel: NSColorSpace.Model { get }
```

```objc
@property (readonly) NSColorSpaceModel colorSpaceModel;
```

## Discussion

See `Color Space Models` for a list of valid NSColorSpaceModel constants.

## See Also

### Accessing Color Space Data and Attributes
- [var cgColorSpace: CGColorSpace?](./cgcolorspace.md)
  The Core Graphics color-space object that represents a color space equivalent to the color space’s.
- [NSColorSpace.Model](./model.md)
  Constants that describe the abstract model on which color space objects are based.
- [var colorSyncProfile: UnsafeMutableRawPointer?](./colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
- [var iccProfileData: Data?](./iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [var localizedName: String?](./localizedname.md)
  The localized name of the color space.
- [var numberOfColorComponents: Int](./numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/colorspacemodel)*