# usesEPSOnResolutionMismatch

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether EPS representations are preferred when no other representations match the resolution of the device.

**Availability**:
- macOS

## Declaration

```swift
var usesEPSOnResolutionMismatch: Bool { get set }
```

```objc
@property BOOL usesEPSOnResolutionMismatch;
```

## Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Setting the Representation Selection Criteria for Images
- [var prefersColorMatch: Bool](./preferscolormatch.md)
  A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.
- [var matchesOnMultipleResolution: Bool](./matchesonmultipleresolution.md)
  A Boolean value that indicates whether image representations whose resolution is an integral multiple of the device resolution are a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/usesepsonresolutionmismatch)*