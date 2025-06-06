# NSTextSelectionNavigation.WritingDirection

**Framework**: UIKit  
**Kind**: enum

Values that describe the writing direction inside a text selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum WritingDirection
```

## Topics

### Writing directions
- [NSTextSelectionNavigation.WritingDirection.leftToRight](nstextselectionnavigation/writingdirection/lefttoright.md)
  The value that defines the left to right writing direction.
- [NSTextSelectionNavigation.WritingDirection.rightToLeft](nstextselectionnavigation/writingdirection/righttoleft.md)
  The value that defines the right to left writing direction.
### Initializers
- [init?(rawValue: Int)](nstextselectionnavigation/writingdirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func baseWritingDirection(at: any NSTextLocation) -> NSTextSelectionNavigation.WritingDirection](nstextselectiondatasource/basewritingdirection(at:).md)
  Returns the base writing direction at the location you specify.
- [func textLayoutOrientation(at: any NSTextLocation) -> NSTextSelectionNavigation.LayoutOrientation](nstextselectiondatasource/textlayoutorientation(at:).md)
  Returns the layout orientation at the location you specify.
- [NSTextSelectionNavigation.LayoutOrientation](nstextselectionnavigation/layoutorientation.md)
  Values that describe the possible layout orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/writingdirection)*