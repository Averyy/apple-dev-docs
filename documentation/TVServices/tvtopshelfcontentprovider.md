# TVTopShelfContentProvider

**Framework**: TV Services  
**Kind**: class

The main interface for your Top Shelf app extension, which you use to provide content for the top shelf area of the tvOS Home Screen.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfContentProvider
```

#### Overview

Adopt this protocol in the principal class of your Top Shelf app extension. Use its methods to create the items that you want to display in the top shelf interface. For each item, specify additional resources such as the image or video to display.

Fill the top shelf area with the user’s active content or with content you want to highlight or promote. For each distinct piece of content, create a [`TVTopShelfCarouselItem`](tvtopshelfcarouselitem.md) or [`TVTopShelfSectionedItem`](tvtopshelfsectioneditem.md) and fill the object with details about that content. For example, provide an identifier for the item and URLs for the pictures or videos you want to display for that item. After creating your items, add them to an appropriate content object and return them from your [`loadTopShelfContent(completionHandler:)`](tvtopshelfcontentprovider/loadtopshelfcontent(completionhandler:).md) method.

## Topics

### Providing the Top Shelf Content
- [func loadTopShelfContent(completionHandler: ((any TVTopShelfContent)?) -> Void)](tvtopshelfcontentprovider/loadtopshelfcontent(completionhandler:).md)
  Provides the content you want to display in the top shelf for your app.
### Updating Your Content
- [class func topShelfContentDidChange()](tvtopshelfcontentprovider/topshelfcontentdidchange.md)
  Tells the system that your top shelf content changed and requires an update.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Building a Full Screen Top Shelf Extension](building-a-full-screen-top-shelf-extension.md)
  Highlight content from your Apple TV application by building a full screen Top Shelf extension.
- [Legacy Extension](legacy-extension.md)
  Help users discover your app by providing top shelf content and a description of your tvOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentprovider)*