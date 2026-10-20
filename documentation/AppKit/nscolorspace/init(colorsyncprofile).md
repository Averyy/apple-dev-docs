# init(colorSyncProfile:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a color space object from the specified ColorSync profile.

**Availability**:
- macOS

## Declaration

```swift
init?(colorSyncProfile prof: UnsafeMutableRawPointer)
```

```objc
- (instancetype) initWithColorSyncProfile:(void *) prof;
```

#### Return Value

The initialized `NSColorSpace` object or `nil` if initialization was not successful.

## Parameters

- `prof`: The ColorSync profile to use when initializing the `NSColorSpace` object. This should be an object of opaque type CMProfileRef. See [ColorSync Manager](../../applicationservices/colorsync_manager.md) for further information on CMProfileRef.

## See Also

### Related Documentation
- [var colorSyncProfile: UnsafeMutableRawPointer?](./colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
### Initializing a Custom Color Space Object
- [init?(cgColorSpace: CGColorSpace)](./init%28cgcolorspace%29-889nv.md)
  Initializes and returns a color space object initialized from a Core Graphics color-space object.
- [init?(iccProfileData: Data)](./init%28iccprofiledata%29-8rl9d.md)
  Initializes and returns a color space object from the specified ICC profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/init(colorsyncprofile:))*