# init(iccProfileData:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a color space object from the specified ICC profile.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(iccProfileData iccData: Data)
```

#### Return Value

The initialized `NSColorSpace` object or `nil` if initialization was not successful.

## Parameters

- `iccData`: The ICC profile to use when initializing the   object. For information on ICC profiles, see the latest ICC specification at the   website.

## See Also

- [var iccProfileData: Data?](nscolorspace/iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [init?(cgColorSpace: CGColorSpace)](nscolorspace/init(cgcolorspace:).md)
  Initializes and returns a color space object initialized from a Core Graphics color-space object.
- [init?(colorSyncProfile: UnsafeMutableRawPointer)](nscolorspace/init(colorsyncprofile:).md)
  Initializes and returns a color space object from the specified ColorSync profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/init(iccprofiledata:))*