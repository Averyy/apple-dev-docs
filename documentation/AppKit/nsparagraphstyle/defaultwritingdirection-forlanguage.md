# defaultWritingDirection(forLanguage:)

**Framework**: AppKit  
**Kind**: method

Returns the default writing direction for the specified language.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func defaultWritingDirection(forLanguage languageName: String?) -> NSWritingDirection
```

#### Return Value

The default writing direction.

## Parameters

- `languageName`: The language specified in ISO language region format. Can be   to return a default writing direction derived from the user’s defaults database.

## See Also

- [var baseWritingDirection: NSWritingDirection](nsparagraphstyle/basewritingdirection.md)
  The base writing direction for the paragraph.
- [enum NSWritingDirection](nswritingdirection.md)
  Constants that specify the writing direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/defaultwritingdirection(forlanguage:))*