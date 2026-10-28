# cgColorSpace

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The Core Graphics color-space object that represents a color space equivalent to the color space’s.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var cgColorSpace: CGColorSpace? { get }
```

```objc
@property (readonly, nullable) CGColorSpaceRef CGColorSpace;
```

## Discussion

The value of this property is a reference to an Core Graphics color-space object ([`CGColorSpace`](../../CoreGraphics/cgcolorspace.md)) or `NULL` if the type of color space represented by the receiver cannot be represented by a `CGColorSpace` object.

## See Also

### Accessing Color Space Data and Attributes
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
- [var numberOfColorComponents: Int](./numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/cgcolorspace)*