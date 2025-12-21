# writingDirection(strategy:)

**Framework**: SwiftUI  
**Kind**: method

A modifier for the default text writing direction strategy in the view hierarchy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View
```

#### Discussion

To control the writing direction explicitly, choose the [`layoutBased`](text/writingdirectionstrategy/layoutbased.md) mode and set the [`layoutDirection`](environmentvalues/layoutdirection.md) to the appropriate value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/writingdirection(strategy:))*