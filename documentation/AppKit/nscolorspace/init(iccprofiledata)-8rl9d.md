# init(iccProfileData:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a color space object from the specified ICC profile.

**Availability**:
- macOS

## Declaration

```swift
init?(iccProfileData iccData: Data)
```

```objc
- (instancetype) initWithICCProfileData:(NSData *) iccData;
```

## Return Value

The initialized `NSColorSpace` object or `nil` if initialization was not successful.

## Parameters

- `iccData`: The ICC profile to use when initializing the `NSColorSpace` object. For information on ICC profiles, see the latest ICC specification at the [International Color Consortium website](http://www.color.org/icc_specs2.html) website.

## See Also

### Related Documentation
- [var iccProfileData: Data?](./iccprofiledata.md)
  The ICC profile data from which the color space was created.
### Initializing a Custom Color Space Object
- [init?(cgColorSpace: CGColorSpace)](./init%28cgcolorspace%29-889nv.md)
  Initializes and returns a color space object initialized from a Core Graphics color-space object.
- [init?(colorSyncProfile: UnsafeMutableRawPointer)](./init%28colorsyncprofile%29.md)
  Initializes and returns a color space object from the specified ColorSync profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/init(iccprofiledata:)-8rl9d)*