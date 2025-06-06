# collectionList

**Framework**: TVML

Contains other layout elements.

#### Overview

Here’s an example of a `collectionList` element that contains a `shelf` and two `lockup` elements.

```xml
<collectionList>
    <shelf>
        <section>
            <lockup>
                <img src="path to images on your server/Car_Movie_250x375_A.png" width="182" height="274" />
                <title>Movie 1</title>
            </lockup>
            <lockup>
                <img src="path to images on your server/Car_Movie_250x375_B.png" width="182" height="274" />
                <title>Movie 2</title>
            </lockup>
        </section>
    </shelf>
</collectionList>
```

##### Subelements of Collectionlist

- [`carousel`](carousel.md)
- [`grid`](grid.md)
- [`shelf`](shelf.md)

##### Elements That Use Collectionlist

- [`searchTemplate`](searchtemplate.md)
- [`stackTemplate`](stacktemplate.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
### Valid TVML Attributes
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [infoList](infolist.md)
  Displays `info` element information in a vertical format.
- [list](list.md)
  Creates a generic container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/collectionlist)*