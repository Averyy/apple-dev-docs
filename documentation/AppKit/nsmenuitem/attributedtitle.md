# attributedTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A custom string for a menu item.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var attributedTitle: NSAttributedString? { get set }
```

```objc
@property (copy, nullable) NSAttributedString * attributedTitle;
```

#### Discussion

The attributed string is not archived in the old nib format.

## See Also

### Managing the title
- [var title: String](./title.md)
  The menu item’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/attributedtitle)*