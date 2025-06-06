# carousel

**Framework**: TVML

Arranges images in a row.

#### Overview

The `carousel` element displays images in a row that the user can navigate by swiping left and right on the remote. Here’s an example that creates a carousel containing three movie scenes that the user can navigate between.

```xml
<carousel>
    <section>
        <lockup>
            <img src="path to images on your server/Car_Movie_453x255_C.png" width="453" height="255" />
            <title>Scene 1</title>
        </lockup>
        <lockup>
            <img src="path to images on your server/Car_Movie_500x600.png" width="500" height="600" />
            <title>Scene 2</title>
        </lockup>
        <lockup>
            <img src="path to images on your server/Car_Movie_308x308_B.png" width="308" height="308" />
            <title>Scene 3</title>
        </lockup>
    </section>
</carousel>
```

##### Subelements of Carousel

- [`section`](section.md)

##### Elements That Use Carousel

- [`collectionList`](collectionlist.md)
- [`showcaseTemplate`](showcasetemplate.md)

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [grid](grid.md)
  Arranges elements in a grid pattern.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/carousel)*