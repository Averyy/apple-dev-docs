# defaultWritingDirection(forLanguage:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the default writing direction for the specified language.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func defaultWritingDirection(forLanguage languageName: String?) -> NSWritingDirection
```

```objc
+ (NSWritingDirection) defaultWritingDirectionForLanguage:(NSString *) languageName;
```

## Return Value

The default writing direction.

## Parameters

- `languageName`: The language specified in ISO language region format. Can be `nil` to return a default writing direction derived from the user’s defaults database.

## See Also

### Determining writing direction
- [var baseWritingDirection: NSWritingDirection](./basewritingdirection.md)
  The base writing direction for the paragraph.
- [enum NSWritingDirection](../nswritingdirection.md)
  Constants that specify the writing direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/defaultwritingdirection(forlanguage:))*