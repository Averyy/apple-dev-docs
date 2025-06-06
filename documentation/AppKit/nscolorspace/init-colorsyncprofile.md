# init(colorSyncProfile:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a color space object from the specified ColorSync profile.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(colorSyncProfile prof: UnsafeMutableRawPointer)
```

#### Return Value

The initialized `NSColorSpace` object or `nil` if initialization was not successful.

## Parameters

- `prof`: The ColorSync profile to use when initializing the   object. This should be an object of opaque type CMProfileRef. See   for further information on CMProfileRef.

## See Also

- [var colorSyncProfile: UnsafeMutableRawPointer?](nscolorspace/colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
- [init?(cgColorSpace: CGColorSpace)](nscolorspace/init(cgcolorspace:).md)
  Initializes and returns a color space object initialized from a Core Graphics color-space object.
- [init?(iccProfileData: Data)](nscolorspace/init(iccprofiledata:).md)
  Initializes and returns a color space object from the specified ICC profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/init(colorsyncprofile:))*