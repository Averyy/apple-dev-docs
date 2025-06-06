# usesEPSOnResolutionMismatch

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether EPS representations are preferred when no other representations match the resolution of the device.

**Availability**:
- macOS ?+

## Declaration

```swift
var usesEPSOnResolutionMismatch: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var prefersColorMatch: Bool](nsimage/preferscolormatch.md)
  A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.
- [var matchesOnMultipleResolution: Bool](nsimage/matchesonmultipleresolution.md)
  A Boolean value that indicates whether image representations whose resolution is an integral multiple of the device resolution are a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/usesepsonresolutionmismatch)*