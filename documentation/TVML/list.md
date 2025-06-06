# list

**Framework**: TVML

Creates a generic container.

#### Overview

The `list` element is a generic element that contains nearly all other elements in the templates that use it. Here’s an example of a `list` inside of a `paradeTemplate`. The `list` element contains the information for the page.

```xml
<paradeTemplate>
    <list>
        <header>
            <title>Movie Genres</title>
        </header>
        <section>
            <listItemLockup>
                <title>Action</title>
            </listItemLockup>
            <listItemLockup>
                <title>Comedy</title>
            </listItemLockup>
        </section>
        <relatedContent>
            <imgDeck>
                <img src="path to images on your server/Car_Movie_250x375.png "/>
                <img src="path to images on your server/Car_Movie_250x375_A.png "/>
                <img src="path to images on your server/Car_Movie_250x375_B.png "/>
                <img src="path to images on your server/Car_Movie_250x375_C.png "/>
            </imgDeck>
        </relatedContent>
    </list>
</paradeTemplate>
```

##### Subelements for List

- [`header`](header.md)
- [`relatedContent`](relatedcontent.md)
- [`section`](section.md)
- [`tumblerBar`](tumblerbar.md)

##### Elements That Use List

- [`catalogTemplate`](catalogtemplate.md)
- [`compilationTemplate`](compilationtemplate.md)
- [`listTemplate`](listtemplate.md)
- [`paradeTemplate`](paradetemplate.md)
- [`searchTemplate`](searchtemplate.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [tv-interitem-spacing](tv-interitem-spacing.md)
  Specifies the spacing between child elements.
- [width](element-shaping-width.md)
  Specifies how wide an element is.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [collectionList](collectionlist.md)
  Contains other layout elements.
- [infoList](infolist.md)
  Displays `info` element information in a vertical format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/list)*