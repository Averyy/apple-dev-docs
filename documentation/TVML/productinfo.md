# productInfo

**Framework**: TVML

Contains general information about a product.

#### Overview

The `productInfo` element contains all of the elements required to describe a product. It commonly contains such information as a product’s title, type, format, running time, and so on. Here’s an example that describes a video, including its run time and languages.

```xml
<productInfo>
    <infoTable>
        <header>
            <title>Information</title>
        </header>
        <info>
            <header>
                <title>Studio</title>
            </header>
            <text>Apple</text>
        </info>
        <info>
            <header>
                <title>Runtime</title>
            </header>
            <text>1:54</text>
        </info>
        <info>
            <header>
                <title>Format</title>
            </header>
            <text>Widescreen</text>
        </info>
    </infoTable>
    <infoTable>
        <header>
            <title>Languages</title>
        </header>
        <info>
            <header>
                <title>Primary</title>
            </header>
            <text>English (Dolby 5.1), Subtitles, CC</text>
        </info>
        <info>
            <header>
                <title>Additional</title>
            </header>
            <text>Cantonese (Subtitles)</text>
        </info>
    </infoTable>
    <infoTable style="tv-line-spacing:10;">
        <header>
            <title>Accessibility</title>
        </header>
        <info>
            <header>
                <textBadge>SDH</textBadge>
            </header>
            <text>Subtitles for the deaf and Hard of Hearing (SDH) refer to subtitles in the original lanuage with the addition of relevant non-dialog information.</text>
        </info>
    </infoTable>
</productInfo>
```

##### Subelements of Productinfo

- [`header`](header.md)
- [`infoTable`](infotable.md)
- [`row`](row.md)
- [`text`](text.md)

##### Elements That Use Productinfo

- [`productBundleTemplate`](productbundletemplate.md)
- [`productTemplate`](producttemplate.md)

## Topics

### Valid TVML Styles
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [tv-interitem-spacing](tv-interitem-spacing.md)
  Specifies the spacing between child elements.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [info](info.md)
  Displays grouped sets of information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/productinfo)*