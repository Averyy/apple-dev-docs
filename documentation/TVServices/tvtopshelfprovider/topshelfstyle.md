# topShelfStyle

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The user interface style that should be used to display the content items.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVTopShelfProvider has been replaced by TVTopShelfContentProvider

## Declaration

```swift
var topShelfStyle: TVTopShelfContentStyle { get }
```

```objc
@property (readonly) TVTopShelfContentStyle topShelfStyle;
```

## See Also

### Implementing TV Services Extension Properties
- [var topShelfItems: [TVContentItem]](./topshelfitems.md)
  Returns an array of content items to be displayed.
- [enum TVTopShelfContentStyle](../tvtopshelfcontentstyle.md)
  An enumerated type used to specify the style in which you want your content to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfprovider/topshelfstyle)*