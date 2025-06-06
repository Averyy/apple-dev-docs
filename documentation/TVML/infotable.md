# infoTable

**Framework**: TVML

Displays contained element information in a vertical format, with each successive element directly below the previous element.

#### Overview

Here’s an example that displays information vertically inside of a `ratingCard` element.

```xml
<ratingCard>
    <title><badge src="resource://tomato-fresh" /> 99%</title>
    <text>Tomatometer</text>
    <infoTable>
        <info>
            <header>
                <title>175</title>
            </header>
            <text>Reviews</text>
        </info>
        <info>
            <header>
                <title>173</title>
            </header>
            <text>Fresh</text>
        </info>
        <info>
            <header>
                <title>2</title>
            </header>
            <text>Rotten</text>
        </info>
    </infoTable>
</ratingCard>
```

##### Subelements of Infotable

- [`footer`](footer.md)
- [`header`](header.md)
- [`info`](info.md)

##### Elements That Use Infotable

- [`descriptiveAlertTemplate`](descriptivealerttemplate.md)
- [`productInfo`](productinfo.md)
- [`ratingCard`](ratingcard.md)
- [`relatedContent`](relatedcontent.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [max-height](element-shaping-max-height.md)
  Specifies the maximum height for an element.
- [tv-line-spacing](tv-line-spacing.md)
  Specifies the amount of space between lines of text.
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
- [organizer](organizer.md)
  Creates a generic element with its contained elements arranged through TVML styles.
- [row](row.md)
  Displays elements horizontally.
- [section](section.md)
  Combines elements and acts as a single element.
- [stack](stack.md)
  Groups and lays out elements vertically.
- [shelf](shelf.md)
  Displays elements horizontally and adds the ability to scroll to offscreen elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/infotable)*