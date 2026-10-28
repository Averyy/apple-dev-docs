# prefersColorMatch

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.

**Availability**:
- macOS

## Declaration

```swift
var prefersColorMatch: Bool { get set }
```

```objc
@property BOOL prefersColorMatch;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the image attempts to match the color capabilities of the rendering device first. When it is [`false`](../../Swift/false.md), the image prefers resolution-matching first. The default value is [`true`](../../Swift/true.md). Both color-matching and resolution-matching may influence the choice of an image representation. You use this method to choose which technique should be used first during the selection process.

## See Also

### Setting the Representation Selection Criteria for Images
- [var usesEPSOnResolutionMismatch: Bool](./usesepsonresolutionmismatch.md)
  A Boolean value that indicates whether EPS representations are preferred when no other representations match the resolution of the device.
- [var matchesOnMultipleResolution: Bool](./matchesonmultipleresolution.md)
  A Boolean value that indicates whether image representations whose resolution is an integral multiple of the device resolution are a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/preferscolormatch)*