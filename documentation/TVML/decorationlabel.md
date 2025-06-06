# decorationLabel

**Framework**: TVML

Displays text that describes a displayed element.

#### Overview

This element is commonly used to provide additional information for a media item or group of media items; for example, the running time for a movie. Here’s an example where the decoration label displays the number of items contained in a `listItemLockup` element.

```xml
<listItemLockup>
    <title>Comedies</title>
    <decorationLabel>4</decorationLabel>
    <relatedContent>
        <grid>
            <section>
                <lockup>
                    <img src="path to images on your server/Car_Movie_250x375_B.png" width="250" height="376" />
                    <title>Movie 2</title>
                </lockup>
                <lockup>
                    <img src="path to images on your server/Car_Movie_250x375_A.png" width="250" height="376" />
                    <title>Movie 1</title>
                </lockup>
                <lockup>
                    <img src="path to images on your server/Car_Movie_250x375.png" width="250" height="376" />
                    <title>Movie 4</title>
                </lockup>
                <lockup>
                    <img src="path to images on your server/Car_Movie_250x375_C.png" width="250" height="376" />
                    <title>Movie 3</title>
                </lockup>
            </section>
        </grid>
    </relatedContent>
</listItemLockup>
```

##### Contained in

- [`listItemLockup`](listitemlockup.md)

## Topics

### Valid TVML Styles
- [color](color.md)
  Changes the color of an element.
- [font-family](font-family.md)
  Specifies the font used for the text in an element.
- [font-size](font-size.md)
  Specifies the font size for the text in an element.
- [font-weight](font-weight.md)
  Specifies the font weight for the text in an element.
- [margin](margin.md)
  Specifies the spacing around an element.
- [max-height](element-shaping-max-height.md)
  Specifies the maximum height for an element.
- [max-width](element-shaping-max-width.md)
  Specifies the maximum width for an element.
- [min-height](element-shaping-min-height.md)
  Specifies the minimum height for an element.
- [min-width](element-shaping-min-width.md)
  Specifies the minimum width for an element.
- [text-align](text-align.md)
  Aligns text horizontally in an element.
- [text-shadow](text-shadow.md)
  Adds a shadow effect to displayed text.
- [tv-highlight-color](tv-highlight-color.md)
  Changes an element’s color when it comes into focus.
- [tv-text-style](tv-text-style.md)
  Sets a predefined size and style for text.
### Valid TVML Attributes
- [accessibilityText](accessibilitytext.md)
  Adds hidden text to an element that is used when VoiceOver is enabled.
- [binding](binding.md)
  Associates information in a data item with an element.
- [height](image-attributes-height.md)
  Specifies the maximum height for an image.
- [opaque](opaque.md)
  Indicates whether an image has a transparent background.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.
- [width](image-attributes-width.md)
  Specifies the maximum width for an image element.

## See Also

- [description](description.md)
  Displays multiple lines of text.
- [date](date.md)
  Displays a date.
- [monogram](monogram.md)
  Displays information below a `monogramLockup` element.
- [ordinal](ordinal.md)
  Displays a number.
- [strike](strike.md)
  Draws a line through the designated text.
- [subtitle](subtitle.md)
  Displays text below the subtitle’s containing element.
- [text](text.md)
  Displays text on the screen.
- [title](title.md)
  Displays a short amount of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/decorationlabel)*