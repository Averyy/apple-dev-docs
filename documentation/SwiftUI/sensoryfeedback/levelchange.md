# levelChange

**Framework**: SwiftUI  
**Kind**: property

Indicates movement between discrete levels of pressure.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static let levelChange: SensoryFeedback
```

#### Discussion

For example, as the user presses a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached.

Only plays feedback on macOS.

## See Also

- [static let alignment: SensoryFeedback](sensoryfeedback/alignment.md)
  Indicates the alignment of a dragged item.
- [static let decrease: SensoryFeedback](sensoryfeedback/decrease.md)
  Indicates that an important value decreased below a significant threshold.
- [static let increase: SensoryFeedback](sensoryfeedback/increase.md)
  Indicates that an important value increased above a significant threshold.
- [static let selection: SensoryFeedback](sensoryfeedback/selection.md)
  Indicates that a UI element’s values are changing.
- [static let pathComplete: SensoryFeedback](sensoryfeedback/pathcomplete.md)
  Indicates a drawn path has completed and/or recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/levelchange)*