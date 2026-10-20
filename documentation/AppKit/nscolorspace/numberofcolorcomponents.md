# numberOfColorComponents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of components, excluding alpha, the color space supports.

**Availability**:
- macOS

## Declaration

```swift
var numberOfColorComponents: Int { get }
```

```objc
@property (readonly) NSInteger numberOfColorComponents;
```

#### Discussion

This value is `0` if the color space isn’t based on `float` components.

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
- [var localizedName: String?](./localizedname.md)
  The localized name of the color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/numberofcolorcomponents)*