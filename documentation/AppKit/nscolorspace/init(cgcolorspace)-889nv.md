# init(cgColorSpace:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a color space object initialized from a Core Graphics color-space object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(cgColorSpace: CGColorSpace)
```

```objc
- (instancetype) initWithCGColorSpace:(CGColorSpaceRef) cgColorSpace;
```

## Return Value

The initialized `NSColorSpace` object or `nil` if initialization was not successful, which might happen if the color space represented by the `CGColorSpace` object is not supported by `NSColorSpace`.

## Discussion

Because `NSColorSpace` might retain or copy the `CGColorSpace` object depending on circumstances, you should not assume pointer equality of the provided object with that returned by [`cgColorSpace`](./cgcolorspace.md). And even if the pointer equality is preserved during runtime, it may not be after the `NSColorSpace` object is archived and unarchived.

## Parameters

- `cgColorSpace`: A reference to a Core Graphics color-space object ([`CGColorSpace`](../../CoreGraphics/cgcolorspace.md)).

## See Also

### Initializing a Custom Color Space Object
- [init?(colorSyncProfile: UnsafeMutableRawPointer)](./init%28colorsyncprofile%29.md)
  Initializes and returns a color space object from the specified ColorSync profile.
- [init?(iccProfileData: Data)](./init%28iccprofiledata%29-8rl9d.md)
  Initializes and returns a color space object from the specified ICC profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/init(cgcolorspace:)-889nv)*