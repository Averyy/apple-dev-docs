# TVElementContentAlignment

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

Location of items inside of an element on the vertical axis.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVElementContentAlignment
```

```c
enum TVElementContentAlignment : NSInteger;
```

## Topics

### Constants
- [TVElementContentAlignmentUndefinded](./tvelementcontentalignmentundefinded.md)
  The alignment has not been defined for the element.
- [TVElementContentAlignment.top](./tvelementcontentalignment/top.md)
  Items are aligned along the top of the element.
- [TVElementContentAlignment.center](./tvelementcontentalignment/center.md)
  Items are aligned in the center of the element.
- [TVElementContentAlignment.bottom](./tvelementcontentalignment/bottom.md)
  Items are aligned along the bottom of the element.
### Enumeration Cases
- [TVElementContentAlignment.undefined](./tvelementcontentalignment/undefined.md)
### Initializers
- [init?(rawValue: Int)](./tvelementcontentalignment/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Aligning and Positioning an Element
- [var alignment: TVElementAlignment](./tvviewelementstyle/alignment.md)
  A value indicating how an item is aligned inside of an element.
- [enum TVElementAlignment](./tvelementalignment.md)
  Location of an item inside of an element on the horizontal axis.
- [var contentAlignment: TVElementContentAlignment](./tvviewelementstyle/contentalignment.md)
  A value indicating how items inside of an element are aligned.
- [var focusMargin: UIEdgeInsets](./tvviewelementstyle/focusmargin.md)
  The amount of space, in pixels, a custom cell requires when it comes into focus.
- [var interitemSpacing: CGFloat](./tvviewelementstyle/interitemspacing.md)
  The spacing, in pixels, between items inside of an element.
- [var margin: UIEdgeInsets](./tvviewelementstyle/margin.md)
  The amount of space, in pixels, between the element and other elements.
- [var padding: UIEdgeInsets](./tvviewelementstyle/padding.md)
  The amount of space, in pixels, between the border and the contents of the element.
- [var position: TVElementPosition](./tvviewelementstyle/position.md)
  A value indicating the position of the element relative to the screen or its containing element.
- [enum TVElementPosition](./tvelementposition.md)
  Location of an element relative to the screen or its containing element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementcontentalignment)*