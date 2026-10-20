# TVTopShelfContentStyle

**Framework**: TV Services  
**Kind**: enum  
**Role**: Enumeration

An enumerated type used to specify the style in which you want your content to be displayed.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVTopShelfProvider has been replaced by TVTopShelfContent

## Declaration

```swift
enum TVTopShelfContentStyle
```

```c
enum TVTopShelfContentStyle : NSInteger;
```

## Topics

### Constants
- [TVTopShelfContentStyle.inset](./tvtopshelfcontentstyle/inset.md)
  When the using the inset style, your extension should return a flat array of TV content items. The images of the content items will take up most of the area of the Top Shelf, which will slowly rotate through the items.
- [TVTopShelfContentStyle.sectioned](./tvtopshelfcontentstyle/sectioned.md)
  When using the sectioned style, your extension should return an array that contains content items that represent sections. Each section object should have an array of content items that represent the available media in that section.
### Initializers
- [init?(rawValue: Int)](./tvtopshelfcontentstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Implementing TV Services Extension Properties
- [var topShelfItems: [TVContentItem]](./tvtopshelfprovider/topshelfitems.md)
  Returns an array of content items to be displayed.
- [var topShelfStyle: TVTopShelfContentStyle](./tvtopshelfprovider/topshelfstyle.md)
  The user interface style that should be used to display the content items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentstyle)*