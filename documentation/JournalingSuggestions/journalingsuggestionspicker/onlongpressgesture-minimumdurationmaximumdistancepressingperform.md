# onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)

**Framework**: Journaling Suggestions  
**Kind**: method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onLongPressGesture(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, pressing: ((Bool) -> Void)? = nil, perform action: @escaping () -> Void) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:))*