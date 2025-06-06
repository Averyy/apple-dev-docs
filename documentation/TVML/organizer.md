# organizer

**Framework**: TVML

Creates a generic element with its contained elements arranged through TVML styles.

#### Overview

The `organizer` element provides the ability to manually arrange its containing elements. The `organizer` element creates a view where the elements it contains are arranged using the `tv-align` and `tv-position` styles. Containing elements are centered by default.

![Layout diagram showing the positions other elements can be placed in.](https://docs-assets.developer.apple.com/published/8ab94a6903cb538652ca1484db33c75a/organizer-1%402x.png)

Elements contained in the same position are arranged from the top of the cell to the bottom, in the same order in which they are specified in the `organizer` element. You can specify a `<background><img /></background>` that displays a background image inside of the `organizer`. The background image is top-aligned and is fitted to the size of the `organizer` while keeping the image’s original aspect ratio. Text wrapping inside of the `organizer` only occurs in the `header`, `center`, and `footer` positions.

##### Subelements of Organizer

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

##### Elements That Use Organizer

- [`banner`](banner.md)
- [`lockup`](lockup.md)
- [`listItemLockup`](listitemlockup.md)
- [`ratingCard`](ratingcard.md)
- [`reviewCard`](reviewcard.md)
- [`row`](row.md)

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
- [imgDeck](imgdeck.md)
  Contains several images to be displayed at a later time.
- [infoTable](infotable.md)
  Displays contained element information in a vertical format, with each successive element directly below the previous element.
- [row](row.md)
  Displays elements horizontally.
- [section](section.md)
  Combines elements and acts as a single element.
- [stack](stack.md)
  Groups and lays out elements vertically.
- [shelf](shelf.md)
  Displays elements horizontally and adds the ability to scroll to offscreen elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/organizer)*