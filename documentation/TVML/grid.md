# grid

**Framework**: TVML

Arranges elements in a grid pattern.

#### Overview

Items inside of the `grid` are displayed in a row that is bound by the size of the screen. Items are automatically moved to another row after a row is filled. Here’s an example of three `lockup` elements inside of a `grid` element.

```xml
<grid>
    <section>
        <lockup>
            <img src="http://localhost:9001/images/Car_Movie_250x375_A.png" width="182" height="274" />
            <title>Movie 1</title>
        </lockup>
        <lockup>
            <img src="http://localhost:9001/images/Car_Movie_250x375_B.png" width="182" height="274" />
            <title>Movie 2</title>
        </lockup>
        <lockup>
            <img src="http://localhost:9001/images/Car_Movie_250x375_C.png" width="182" height="274" />
            <title>Movie 3</title>
        </lockup>
    </section>
</grid>
```

##### Subelements of Grid

- [`header`](header.md)
- [`section`](section.md)

##### Elements That Use Grid

- [`collectionList`](collectionlist.md)
- [`relatedContent`](relatedcontent.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [tv-interitem-spacing](tv-interitem-spacing.md)
  Specifies the spacing between child elements.
- [tv-line-spacing](tv-line-spacing.md)
  Specifies the amount of space between lines of text.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
- [itemID](itemid.md)
  Mark elements for reuse during DOM updates.
- [needsMoreThreshold](needsmorethreshold.md)
  Sets the amount of remaining screen lengths before firing the needs more event.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [carousel](carousel.md)
  Arranges images in a row.
- [imgDeck](imgdeck.md)
  Contains several images to be displayed at a later time.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/grid)*