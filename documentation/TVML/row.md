# row

**Framework**: TVML

Displays elements horizontally.

#### Overview

The `row` element provides the ability to place elements next to other elements horizontally. Elements are displayed left to right in the order they are listed inside of the `row` element. Here’s an example that places two buttons inside of a `row` element.

```xml
<row>
    <buttonLockup>
        <badge src="resource://button-preview" />
        <title>Preview</title>
    </buttonLockup>
    <buttonLockup type="buy">
        <text>$9.99</text>
        <title>Buy</title>
    </buttonLockup>
</row>
```

##### Subelements of Row

- [`badge`](badge.md)
- [`button`](button.md)
- [`buttonLockup`](buttonlockup.md)
- [`organizer`](organizer.md)
- [`subtitle`](subtitle.md)
- [`text`](text.md)

##### Elements That Use Row

- [`banner`](banner.md)
- [`descriptiveAlertTemplate`](descriptivealerttemplate.md)
- [`info`](info.md)
- [`itemBanner`](itembanner.md)
- [`stack`](stack.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [tv-content-align](tv-content-align.md)
  Aligns an element vertically inside its parent element.
- [tv-interitem-spacing](tv-interitem-spacing.md)
  Specifies the spacing between child elements.
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
- [section](section.md)
  Combines elements and acts as a single element.
- [stack](stack.md)
  Groups and lays out elements vertically.
- [shelf](shelf.md)
  Displays elements horizontally and adds the ability to scroll to offscreen elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/row)*