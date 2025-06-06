# init(style:items:)

**Framework**: TV Services  
**Kind**: init

Creates a content object for displaying items in a carousel style in the top shelf interface.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
init(style: TVTopShelfCarouselContent.Style, items: [TVTopShelfCarouselItem])
```

#### Return Value

A new carousel content object containing the specified items.

## Parameters

- `style`: The appearance to use for individual items. For a list of possible values, see  .
- `items`: The items to display in the Top Shelf interface. All of the items in the array must have unique identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselcontent/init(style:items:))*