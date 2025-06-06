# listItemLockup

**Framework**: TVML

Contains a new list item.

#### Overview

The `listItemLockup` subelements are arranged using the `tv-align` and `tv-position` styles. Containing elements are centered by default.

![Layout diagram showing the positions other elements can be placed in.](https://docs-assets.developer.apple.com/published/8ab94a6903cb538652ca1484db33c75a/listitemlockup-1%402x.png)

Elements contained in the same position are arranged from the top of the cell to the bottom, in the same order in which they are specified in the `listItemLockup` element. You can specify a `<background><img /></background>` that displays a background image inside of the `listItemLockup`. The background image is top-aligned and is fitted to the size of the `listItemLockup` while keeping the image’s original aspect ratio. Text wrapping inside of the `listItemLockup` only occurs in the `header`, `center`, and `footer` positions. Here is an example of a two `listItemLockup` elements inside a `section` element.

```xml
<section>
    <listItemLockup>
        <ordinal minLength="2">1</ordinal>
        <title>Opening sequence</title>
        <decorationLabel>11:14</decorationLabel>
    </listItemLockup>
    <listItemLockup>
        <ordinal minLength="2">2</ordinal>
        <title>Fight song</title>
        <decorationLabel>3:47</decorationLabel>
    </listItemLockup>
</section>
```

##### Subelements of Listitemlockup

- [`decorationImage`](decorationimage.md)
- [`decorationLabel`](decorationlabel.md)
- [`img`](img.md)
- [`ordinal`](ordinal.md)
- [`organizer`](organizer.md)
- [`placeholder`](placeholder.md)
- [`relatedContent`](relatedcontent.md)
- [`row`](row.md)
- [`subtitle`](subtitle.md)
- [`title`](title.md)

##### Elements That Use Listitemlockup

- [`section`](section.md)

## Topics

### Valid TVML Styles
- [height](element-shaping-height.md)
  Specifies the height of an element.
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [tv-highlight-color](tv-highlight-color.md)
  Changes an element’s color when it comes into focus.
- [tv-position](tv-position.md)
  Sets the position of an element inside of its parent element.
### Valid TVML Attributes
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
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
- [lockup](lockup.md)
  Contains several elements that are treated as a single element.
- [monogramLockup](monogramlockup.md)
  Creates a monogram using a person’s image or initials.
- [overlay](overlay.md)
  Displays elements on top of other elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/listitemlockup)*