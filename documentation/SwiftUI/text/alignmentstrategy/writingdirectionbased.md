# writingDirectionBased

**Framework**: SwiftUI  
**Kind**: property

The alignment following the writing direction of the same paragraph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static let writingDirectionBased: Text.AlignmentStrategy
```

#### Discussion

When [`multilineTextAlignment`](environmentvalues/multilinetextalignment.md) is [`TextAlignment.leading`](textalignment/leading.md), alignment follows the writing direction. If the value is [`TextAlignment.trailing`](textalignment/trailing.md) alignment is the opposite of the writing direction and finally, a [`TextAlignment.center`](textalignment/center.md) value always results in centered alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/alignmentstrategy/writingdirectionbased)*