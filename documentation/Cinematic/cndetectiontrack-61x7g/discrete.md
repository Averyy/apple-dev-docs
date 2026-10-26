# discrete

**Framework**: Cinematic  
**Kind**: property  
**Role**: Instance Property

A flag determining if the detection track has discrete detections, otherwise continuous.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@property (readonly, getter=isDiscrete) BOOL discrete;
```

#### Discussion

A discrete detection track returns detections only at the specific times a detection occurs. A continuous detection track returns a detection for any requested time and an empty array for time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontrack-61x7g/discrete)*