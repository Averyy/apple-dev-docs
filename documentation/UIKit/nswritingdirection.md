# NSWritingDirection

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSWritingDirection : NSInteger;
```

## Topics

### Constants
- [NSWritingDirection.natural](./nswritingdirection/natural.md)
  The writing direction of the current script that the system determines using the Unicode Bidi Algorithm rules P2 and P3.
- [NSWritingDirection.leftToRight](./nswritingdirection/lefttoright.md)
  The writing direction is left to right.
- [NSWritingDirection.rightToLeft](./nswritingdirection/righttoleft.md)
  The writing direction is right to left.
### Initializers
- [init?(rawValue: Int)](./nswritingdirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining writing direction
- [class func defaultWritingDirection(forLanguage: String?) -> NSWritingDirection](./nsparagraphstyle/defaultwritingdirection%28forlanguage%29.md)
  Returns the default writing direction for the specified language.
- [var baseWritingDirection: NSWritingDirection](./nsparagraphstyle/basewritingdirection.md)
  The base writing direction for the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nswritingdirection)*