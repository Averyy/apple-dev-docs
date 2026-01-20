# init(rawValue:)

**Framework**: RealityKit  
**Kind**: init

Creates a fill mode from its backing data type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(rawValue: Int8)
```

#### Discussion

Use this initializer to unarchive a fill mode from data:

```swift
let rawValue = unarchiveNextInt8(from: data) // Pseudo code.
let fillMode = AnimationFillMode(rawValue: rawValue)
```

## Parameters

- `rawValue`: The backing data value for the fill mode.

## See Also

- [static let none: AnimationFillMode](animationfillmode/none.md)
  An option that indicates an animation doesn’t display frame data outside of its normal duration.
- [static let forwards: AnimationFillMode](animationfillmode/forwards.md)
  An option that freezes the last frame of the animation until it stops.
- [static let backwards: AnimationFillMode](animationfillmode/backwards.md)
  An option that shows the first animation frame while playback progresses to the beginning position.
- [static let both: AnimationFillMode](animationfillmode/both.md)
  An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/init(rawvalue:))*