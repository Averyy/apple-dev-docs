# NSTextSelectionNavigation.LayoutOrientation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe the possible layout orientations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum LayoutOrientation
```

```c
enum NSTextSelectionNavigationLayoutOrientation : NSInteger;
```

## Topics

### Layout orientations
- [NSTextSelectionNavigation.LayoutOrientation.horizontal](./layoutorientation/horizontal.md)
  The value that defines horizontal layout orientation.
- [NSTextSelectionNavigation.LayoutOrientation.vertical](./layoutorientation/vertical.md)
  The value that defines vertical layout orientation.
### Initializers
- [init?(rawValue: Int)](./layoutorientation/init%28rawvalue%29.md)

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
- [NSTextSelectionNavigation.WritingDirection](./writingdirection.md)
  Values that describe the writing direction inside a text selection.
- [func textLayoutOrientation(at: any NSTextLocation) -> NSTextSelectionNavigation.LayoutOrientation](../nstextselectiondatasource/textlayoutorientation%28at%29.md)
  Returns the layout orientation at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/layoutorientation)*