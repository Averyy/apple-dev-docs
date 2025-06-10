# isDiscrete

**Framework**: Cinematic  
**Kind**: property

A flag determining if the detection track has discrete detections, otherwise continuous.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var isDiscrete: Bool { get }
```

#### Discussion

A discrete detection track returns detections only at the specific times a detection occurs. A continuous detection track returns a detection for any requested time and an empty array for time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontrack-2bxtd/isdiscrete)*