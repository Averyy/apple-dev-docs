# iccProfileData

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The ICC profile data from which the color space was created.

**Availability**:
- macOS

## Declaration

```swift
var iccProfileData: Data? { get }
```

```objc
@property (strong, readonly, nullable) NSData * ICCProfileData;
```

## Discussion

The ICC profile from which the receiver was created. This method attempts to compute the profile data from a CMProfileRef object and returns `nil` if it is unable to.

For information on ICC profiles, see the latest ICC specification at the [International Color Consortium website](http://www.color.org/icc_specs2.html).

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
- [var localizedName: String?](./localizedname.md)
  The localized name of the color space.
- [var numberOfColorComponents: Int](./numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/iccprofiledata)*