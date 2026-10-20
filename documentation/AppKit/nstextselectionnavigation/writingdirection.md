# NSTextSelectionNavigation.WritingDirection

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe the writing direction inside a text selection.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum WritingDirection
```

```c
enum NSTextSelectionNavigationWritingDirection : NSInteger;
```

## Topics

### Writing directions
- [NSTextSelectionNavigation.WritingDirection.leftToRight](./writingdirection/lefttoright.md)
  The value that defines the left to right writing direction.
- [NSTextSelectionNavigation.WritingDirection.rightToLeft](./writingdirection/righttoleft.md)
  The value that defines the right to left writing direction.
### Initializers
- [init?(rawValue: Int)](./writingdirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Changing the characteristics of the selection
- [func baseWritingDirection(at: any NSTextLocation) -> NSTextSelectionNavigation.WritingDirection](../nstextselectiondatasource/basewritingdirection%28at%29.md)
  Returns the base writing direction at the location you specify.
- [func textLayoutOrientation(at: any NSTextLocation) -> NSTextSelectionNavigation.LayoutOrientation](../nstextselectiondatasource/textlayoutorientation%28at%29.md)
  Returns the layout orientation at the location you specify.
- [NSTextSelectionNavigation.LayoutOrientation](./layoutorientation.md)
  Values that describe the possible layout orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/writingdirection)*