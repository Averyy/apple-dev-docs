# stack

**Framework**: TVML

Groups and lays out elements vertically.

#### Overview

The `stack` element groups elements together and lays them out vertically, starting from the top of the containing element. Each element is placed directly underneath the preceding element.

```xml
<stack>
    <title>WWDC Road Trip</title>
    <row>
        <text><badge src="resource://tomato-fresh"/> 99%</text>
        <text>1hr 54min</text>
        <text>Comedy</text>
        <text>2015</text>
        <badge src="resource://mpaa-pg" class="badge" />
        <badge src="resource://cc" class="badge" />
    </row>
    <description handlesOverflow="true">An aspiring developer gets a ticket to WWDC, but can't afford to fly there. Now they need to get across country in time for the keynote, and the only person who can help is their quirky roommate.</description>
    <text>Language information can go here</text>
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
</stack>
```

##### Subelements of Stack

- [`description`](description.md)
- [`ratingCard`](ratingcard.md)
- [`reviewCard`](reviewcard.md)
- [`row`](row.md)
- [`subtitle`](subtitle.md)
- [`text`](text.md)
- [`title`](title.md)

##### Elements That Use Stack

- [`banner`](banner.md)
- [`shelf`](shelf.md)

## Topics

### Valid TVML Styles
- [height](element-shaping-height.md)
  Specifies the height of an element.
- [margin](margin.md)
  Specifies the spacing around an element.
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
- [section](section.md)
  Combines elements and acts as a single element.
- [shelf](shelf.md)
  Displays elements horizontally and adds the ability to scroll to offscreen elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/stack)*