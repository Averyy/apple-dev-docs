# matchesOnMultipleResolution

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether image representations whose resolution is an integral multiple of the device resolution are a match.

**Availability**:
- macOS

## Declaration

```swift
var matchesOnMultipleResolution: Bool { get set }
```

```objc
@property BOOL matchesOnMultipleResolution;
```

## Discussion

When this property is set to [`false`](../../Swift/false.md), only image representations whose resolution is exactly the same as the device resolution are matches. If the property is set to [`true`](../../Swift/true.md) and multiple image representations fit this criteria, the one whose resolution is closest to the device resolution is chosen.

The default value is [`true`](../../Swift/true.md).

## See Also

### Setting the Representation Selection Criteria for Images
- [var prefersColorMatch: Bool](./preferscolormatch.md)
  A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.
- [var usesEPSOnResolutionMismatch: Bool](./usesepsonresolutionmismatch.md)
  A Boolean value that indicates whether EPS representations are preferred when no other representations match the resolution of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/matchesonmultipleresolution)*