# card

**Framework**: TVML

Creates a generic element with its contained elements arranged through TVML styles.

#### Overview

The `card` element provides the ability to manually arrange its containing elements. It creates a view where the elements it contains are arranged using the `tv-align` and `tv-position` styles. Containing elements are centered by default.

![Layout diagram showing the positions other elements can be placed in.](https://docs-assets.developer.apple.com/published/8ab94a6903cb538652ca1484db33c75a/card-1%402x.png)

Elements contained in the same position are arranged from the top of the cell to the bottom, in the same order in which they are specified in the `card` element. You can specify a `<background><img /></background>` that displays a background image inside of the `card`. The background image is top-aligned and is fitted to the size of the `card` while keeping the image’s original aspect ratio. Text wrapping inside of the `card` only occurs in the `header`, `center`, and `footer` positions.

##### Subelements of Card

- [`background`](background.md)
- [`badge`](badge.md)
- [`button`](button.md)
- [`buttonLockup`](buttonlockup.md)
- [`img`](img.md)
- [`ordinal`](ordinal.md)
- [`placeholder`](placeholder.md)
- [`ratingBadge`](ratingbadge.md)
- [`row`](row.md)
- [`seasonBadge`](seasonbadge.md)
- [`text`](text.md)
- [`textBadge`](textbadge.md)

##### Elements That Use Card

- [`grid`](grid.md)
- [`shelf`](shelf.md)

## Topics

### Valid TVML Styles
- [border-radius](border-radius.md)
  Changes the shape of an element’s corner.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [reviewCard](reviewcard.md)
  Displays abbreviated review information for a media item.
- [ratingCard](ratingcard.md)
  Contains rating information about a product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/card)*