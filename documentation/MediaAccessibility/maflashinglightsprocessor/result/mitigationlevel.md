# mitigationLevel

**Framework**: Media Accessibility  
**Kind**: property

The amount of mitigation in the output surface.

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
var mitigationLevel: Float { get }
```

#### Discussion

The result is a value between `0` and `100`, where `100` is the highest level of mitigation that can apply to the output surface, indicating the output is completely dark.

## See Also

- [var surfaceProcessed: Bool](maflashinglightsprocessor/result/surfaceprocessed.md)
  A Boolean value that indicates whether the flashing lights processor successfully processed the input surface.
- [var intensityLevel: Float](maflashinglightsprocessor/result/intensitylevel.md)
  The intensity of flashing lights in the input surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/result/mitigationlevel)*