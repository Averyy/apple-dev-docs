# only(_:)

**Framework**: AVKit  
**Kind**: method

Returns a set of experiences for the provided list.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func only<C>(_ experiences: C) -> AVExperienceController.Experiences where C : Collection, C.Element == AVExperienceController.Experience
```

#### Discussion

Use this method when the use case requires a specific set of experiences.

## Parameters

- `experiences`: The experiences to include. Order and duplication are not significant.

## See Also

- [static func recommended<C>(excluding: C, including: C) -> AVExperienceController.Experiences](avexperiencecontroller/experiences/recommended(excluding:including:).md)
  Returns the recommended set of experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experiences/only(_:))*