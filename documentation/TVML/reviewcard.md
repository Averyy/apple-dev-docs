# reviewCard

**Framework**: TVML

Displays abbreviated review information for a media item.

#### Overview

Here’s a general example for a movie review.

```xml
<reviewCard>
    <badge src="resource://tomato-fresh-m" />
    <title>WWDC Review</title>
    <description>Brief review here</description>
    <text>Ravi Patel June, 8 2015</text>
</reviewCard>
```

##### Subelements of Reviewcard

- [`badge`](badge.md)
- [`description`](description.md)
- [`img`](img.md)
- [`organizer`](organizer.md)
- [`ratingBadge`](ratingbadge.md)
- [`text`](text.md)
- [`title`](title.md)

##### Elements That Use Reviewcard

- [`section`](section.md)

## Topics

### Valid TVML Styles
- [background-color](background-color.md)
  Changes the background color of an element.
- [border-radius](border-radius.md)
  Changes the shape of an element’s corner.
- [height](element-shaping-height.md)
  Specifies the height of an element.
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [tv-highlight-color](tv-highlight-color.md)
  Changes an element’s color when it comes into focus.
- [tv-position](tv-position.md)
  Sets the position of an element inside of its parent element.
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

- [card](card.md)
  Creates a generic element with its contained elements arranged through TVML styles.
- [ratingCard](ratingcard.md)
  Contains rating information about a product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/reviewcard)*