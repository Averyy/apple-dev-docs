# section

**Framework**: TVML

Combines elements and acts as a single element.

#### Overview

The `section` element groups elements together so they can be treated as a single element for layout purposes. Here’s an example that uses a section to hold two movie `lockup` elements and places them in a `shelf` element.

```xml
<shelf>
    <header>
        <title>Viewers Also Watched</title>
    </header>
    <section>
        <lockup>
            <img src="path to images on your server/Car_Movie_250x375_A.png" width="150" height="226" />
            <title>Turn</title>
        </lockup>
        <lockup>
            <img src="path to images on your server/Car_Movie_250x375_B.png" width="150" height="226" />
            <title>Road</title>
        </lockup>
    </section>
</shelf>
```

##### Subelements of Section

- [`header`](header.md)
- [`listItemLockup`](listitemlockup.md)
- [`lockup`](lockup.md)
- [`menuItem`](menuitem.md)

##### Elements That Use Section

- [`carousel`](carousel.md)
- [`grid`](grid.md)
- [`list`](list.md)
- [`menuBar`](menubar.md)
- [`oneupTemplate`](oneuptemplate.md)
- [`shelf`](shelf.md)

## Topics

### Valid TVML Styles
- [tv-interitem-spacing](tv-interitem-spacing.md)
  Specifies the spacing between child elements.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [indexTitles](indextitles.md)
  Specifies index bar titles for a section element.
- [itemID](itemid.md)
  Mark elements for reuse during DOM updates.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [carousel](carousel.md)
  Arranges images in a row.
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
- [stack](stack.md)
  Groups and lays out elements vertically.
- [shelf](shelf.md)
  Displays elements horizontally and adds the ability to scroll to offscreen elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/section)*