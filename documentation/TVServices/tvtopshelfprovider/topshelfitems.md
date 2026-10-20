# topShelfItems

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns an array of content items to be displayed.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVTopShelfProvider has been replaced by TVTopShelfContentProvider

## Declaration

```swift
var topShelfItems: [TVContentItem] { get }
```

```objc
@property (readonly) NSArray<TVContentItem *> * topShelfItems;
```

#### Discussion

If the value is an empty array, the system falls back to the static image provided with the app.

## See Also

### Implementing TV Services Extension Properties
- [var topShelfStyle: TVTopShelfContentStyle](./topshelfstyle.md)
  The user interface style that should be used to display the content items.
- [enum TVTopShelfContentStyle](../tvtopshelfcontentstyle.md)
  An enumerated type used to specify the style in which you want your content to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfprovider/topshelfitems)*