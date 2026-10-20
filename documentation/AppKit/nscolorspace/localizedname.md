# localizedName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The localized name of the color space.

**Availability**:
- macOS

## Declaration

```swift
var localizedName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * localizedName;
```

#### Discussion

This property holds the name of the color space as a localized string or `nil` if no localized name exists.

## See Also

### Accessing Color Space Data and Attributes
- [var cgColorSpace: CGColorSpace?](./cgcolorspace.md)
  The Core Graphics color-space object that represents a color space equivalent to the color space’s.
- [var colorSpaceModel: NSColorSpace.Model](./colorspacemodel.md)
  The model on which the color space is based.
- [NSColorSpace.Model](./model.md)
  Constants that describe the abstract model on which color space objects are based.
- [var colorSyncProfile: UnsafeMutableRawPointer?](./colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
- [var iccProfileData: Data?](./iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [var numberOfColorComponents: Int](./numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/localizedname)*