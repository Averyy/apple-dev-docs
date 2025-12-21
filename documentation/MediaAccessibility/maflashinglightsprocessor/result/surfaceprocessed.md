# surfaceProcessed

**Framework**: Media Accessibility  
**Kind**: property

A Boolean value that indicates whether the flashing lights processor successfully processed the input surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var surfaceProcessed: Bool { get }
```

#### Discussion

This value is [`false`](https://developer.apple.com/documentation/Swift/false) if the flashing lights processor can’t process the surface, which can occur for unsupported hardware or unsupported color spaces.

## See Also

- [var intensityLevel: Float](maflashinglightsprocessor/result/intensitylevel.md)
  The intensity of flashing lights in the input surface.
- [var mitigationLevel: Float](maflashinglightsprocessor/result/mitigationlevel.md)
  The amount of mitigation in the output surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/result/surfaceprocessed)*