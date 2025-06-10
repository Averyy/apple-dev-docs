# NSWritingDirection

**Framework**: UIKit  
**Kind**: enum

Constants that specify the writing direction.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum NSWritingDirection
```

## Topics

### Constants
- [NSWritingDirection.natural](nswritingdirection/natural.md)
  The writing direction of the current script that the system determines using the Unicode Bidi Algorithm rules P2 and P3.
- [NSWritingDirection.leftToRight](nswritingdirection/lefttoright.md)
  The writing direction is left to right.
- [NSWritingDirection.rightToLeft](nswritingdirection/righttoleft.md)
  The writing direction is right to left.
### Initializers
- [init?(rawValue: Int)](nswritingdirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func defaultWritingDirection(forLanguage: String?) -> NSWritingDirection](nsparagraphstyle/defaultwritingdirection(forlanguage:).md)
  Returns the default writing direction for the specified language.
- [var baseWritingDirection: NSWritingDirection](nsparagraphstyle/basewritingdirection.md)
  The base writing direction for the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nswritingdirection)*