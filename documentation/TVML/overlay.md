# overlay

**Framework**: TVML

Displays elements on top of other elements.

#### Overview

The `overlay` element provides the ability to place elements on top of images contained within a `lockup` element. The `overlay` element superimposes the elements it contains over an image. The `overlay` element creates a view where the elements it contains are arranged using the `tv-align` and `tv-position` styles. Containing elements are centered by default.

![Layout diagram showing the positions other elements can be placed in.](https://docs-assets.developer.apple.com/published/8ab94a6903cb538652ca1484db33c75a/overlay-1%402x.png)

Elements contained in the same position are arranged from the top of the cell to the bottom, in the same order in which they are specified in the `overlay` element. You can specify a `<background><img /></background>` that displays a background image inside of the `overlay`. The background image is top-aligned and is fitted to the size of the `overlay` while keeping the image’s original aspect ratio. Text wrapping inside of the `overlay` only occurs in the `header`, `center`, and `footer` positions.

##### Subelements of Overlay

- [`badge`](badge.md)
- [`description`](description.md)
- [`progressBar`](progressbar.md)
- [`subtitle`](subtitle.md)
- [`title`](title.md)

##### Elements That Use Overlay

- [`lockup`](lockup.md)

## Topics

### Valid TVML Styles
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [tv-position](tv-position.md)
  Sets the position of an element inside of its parent element.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [button](button.md)
  Displays a button icon the user can click to initiate an action.
- [buttonLockup](buttonlockup.md)
  Creates a button that can also have a badge associated with it.
- [listItemLockup](listitemlockup.md)
  Contains a new list item.
- [lockup](lockup.md)
  Contains several elements that are treated as a single element.
- [monogramLockup](monogramlockup.md)
  Creates a monogram using a person’s image or initials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/overlay)*