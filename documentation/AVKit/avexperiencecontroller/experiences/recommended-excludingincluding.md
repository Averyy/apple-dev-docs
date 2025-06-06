# recommended(excluding:including:)

**Framework**: AVKit  
**Kind**: method

Returns the recommended set of experiences.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func recommended<C>(excluding: C = [], including: C = []) -> AVExperienceController.Experiences where C : Collection, C.Element == AVExperienceController.Experience
```

#### Discussion

Use this method to return the default recommended set of experiences for each platform and SDK version. Include or exclude experiences specifically desired or not supported by your app.

## Parameters

- `excluding`: The experiences to remove. Removal happens before adding.
- `including`: The experiences to add. Redundant items are ignored.

## See Also

- [static func only<C>(C) -> AVExperienceController.Experiences](avexperiencecontroller/experiences/only(_:).md)
  Returns a set of experiences for the provided list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experiences/recommended(excluding:including:))*