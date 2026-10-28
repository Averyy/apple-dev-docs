# selection

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Indicates that a UI element’s values are changing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
static let selection: SensoryFeedback
```

## Discussion

Equivalent to [`selection(_:)`](./selection%28_%29.md) with `SelectionFeedback/default`.

Only plays feedback on iOS and watchOS.

## See Also

### Indicating changes and selections
- [static let alignment: SensoryFeedback](./alignment.md)
  Indicates the alignment of a dragged item.
- [static let decrease: SensoryFeedback](./decrease.md)
  Indicates that an important value decreased below a significant threshold.
- [static let increase: SensoryFeedback](./increase.md)
  Indicates that an important value increased above a significant threshold.
- [static let levelChange: SensoryFeedback](./levelchange.md)
  Indicates movement between discrete levels of pressure.
- [static let pathComplete: SensoryFeedback](./pathcomplete.md)
  Indicates a drawn path has completed and/or recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/selection)*