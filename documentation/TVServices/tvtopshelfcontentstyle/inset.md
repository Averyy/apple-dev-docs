# TVTopShelfContentStyle.inset

**Framework**: TV Services  
**Kind**: case  
**Role**: Case

When the using the inset style, your extension should return a flat array of TV content items. The images of the content items will take up most of the area of the Top Shelf, which will slowly rotate through the items.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVTopShelfProvider has been replaced by TVTopShelfContent

## Declaration

```swift
case inset
```

```c
TVTopShelfContentStyleInset
```

## See Also

### Constants
- [TVTopShelfContentStyle.sectioned](./sectioned.md)
  When using the sectioned style, your extension should return an array that contains content items that represent sections. Each section object should have an array of content items that represent the available media in that section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentstyle/inset)*