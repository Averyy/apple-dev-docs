# baseWritingDirection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The base writing direction for the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var baseWritingDirection: NSWritingDirection { get }
```

```objc
@property (readonly) NSWritingDirection baseWritingDirection;
```

#### Discussion

If you the value of this property is [`NSWritingDirection.natural`](../nswritingdirection/natural.md), the receiver resolves the writing direction to either [`NSWritingDirection.leftToRight`](../nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](../nswritingdirection/righttoleft.md), depending on the direction for the user’s language preference setting.

## See Also

### Determining writing direction
- [class func defaultWritingDirection(forLanguage: String?) -> NSWritingDirection](./defaultwritingdirection%28forlanguage%29.md)
  Returns the default writing direction for the specified language.
- [enum NSWritingDirection](../nswritingdirection.md)
  Constants that specify the writing direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/basewritingdirection)*