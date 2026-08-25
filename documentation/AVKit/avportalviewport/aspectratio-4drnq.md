# aspectRatio

**Framework**: AVKit  
**Kind**: property

The width-to-height ratio of the portal frame.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var aspectRatio: Double? { get set }
```

#### Discussion

Common aspect ratios include:

- 1.78 (16:9) for standard widescreen content
- 2.35 or 2.39 for cinematic widescreen content
- 1.33 (4:3) for traditional content

When this property is `nil`, the system defaults to a 16:9 (1.78) aspect ratio.

> **Note**: The system may adjust values outside typical ranges to ensure a comfortable viewing experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avportalviewport/aspectratio-4drnq)*