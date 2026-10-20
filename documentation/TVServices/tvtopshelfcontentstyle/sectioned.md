# TVTopShelfContentStyle.sectioned

**Framework**: TV Services  
**Kind**: case  
**Role**: Case

When using the sectioned style, your extension should return an array that contains content items that represent sections. Each section object should have an array of content items that represent the available media in that section.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVTopShelfProvider has been replaced by TVTopShelfContent

## Declaration

```swift
case sectioned
```

```c
TVTopShelfContentStyleSectioned
```

## See Also

### Constants
- [TVTopShelfContentStyle.inset](./inset.md)
  When the using the inset style, your extension should return a flat array of TV content items. The images of the content items will take up most of the area of the Top Shelf, which will slowly rotate through the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentstyle/sectioned)*