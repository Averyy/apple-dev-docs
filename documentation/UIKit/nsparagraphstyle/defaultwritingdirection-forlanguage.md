# defaultWritingDirection(forLanguage:)

**Framework**: UIKit  
**Kind**: method

Returns the default writing direction for the specified language.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/defaultwritingdirection(forlanguage:))*