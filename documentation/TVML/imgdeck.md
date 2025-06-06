# imgDeck

**Framework**: TVML

Contains several images to be displayed at a later time.

#### Overview

The `imgDeck` contains a set of `img` elements—images that are part of the related content for another element. When another element, such as `listItemLockup`, is in focus, the information in the `relatedContent` element is also displayed.

```xml
<relatedContent>
    <imgDeck>
        <img src="path to images on your server/Car_Movie_250x375.png "/>
        <img src="path to images on your server/Car_Movie_250x375_A.png "/>
        <img src="path to images on your server/Car_Movie_250x375_B.png "/>
        <img src="path to images on your server/Car_Movie_250x375_C.png "/>
    </imgDeck>
</relatedContent>
```

##### Subelements of Imgdeck

- [`img`](img.md)

##### Elements That Use Imgdeck

- [`relatedContent`](relatedcontent.md)

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [carousel](carousel.md)
  Arranges images in a row.
- [grid](grid.md)
  Arranges elements in a grid pattern.
- [infoTable](infotable.md)
  Displays contained element information in a vertical format, with each successive element directly below the previous element.
- [organizer](organizer.md)
  Creates a generic element with its contained elements arranged through TVML styles.
- [row](row.md)
  Displays elements horizontally.
- [section](section.md)
  Combines elements and acts as a single element.
- [stack](stack.md)
  Groups and lays out elements vertically.
- [shelf](shelf.md)
  Displays elements horizontally and adds the ability to scroll to offscreen elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/imgdeck)*