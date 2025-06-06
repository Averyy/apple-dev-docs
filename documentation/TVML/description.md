# description

**Framework**: TVML

Displays multiple lines of text.

#### Overview

The `description` element contains text used to describe a displayed element. This element is often used to provide descriptions that are significantly longer than those contained in the `text` element. Here’s an example that uses the `descriptiveAlertTemplate` to list an app’s Terms of Service.

```xml
<descriptiveAlertTemplate>
   <title>Terms of Service</title>
   <description>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</description>
   <row>
      ...
   </row>
</descriptiveAlertTemplate>
```

##### Contained in

- [`alertTemplate`](alerttemplate.md)
- [`banner`](banner.md)
- [`descriptiveAlertTemplate`](descriptivealerttemplate.md)
- [`header`](header.md)
- [`lockup`](lockup.md)
- [`overlay`](overlay.md)
- [`relatedContent`](relatedcontent.md)
- [`reviewCard`](reviewcard.md)
- [`section`](section.md)
- [`stackTemplate`](stacktemplate.md)

## Topics

### Valid TVML Styles
- [background-color](background-color.md)
  Changes the background color of an element.
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
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [text-align](text-align.md)
  Aligns text horizontally in an element.
- [text-shadow](text-shadow.md)
  Adds a shadow effect to displayed text.
- [tv-highlight-color](tv-highlight-color.md)
  Changes an element’s color when it comes into focus.
- [tv-minimum-scale-factor](tv-minimum-scale-factor.md)
  Sets the minimum size for text.
- [tv-text-max-lines](tv-text-max-lines.md)
  Specifies the maximum number of lines of text in an element.
- [tv-text-style](tv-text-style.md)
  Sets a predefined size and style for text.
- [width](element-shaping-width.md)
  Specifies how wide an element is.
### Valid TVML Attributes
- [accessibilityText](accessibilitytext.md)
  Adds hidden text to an element that is used when VoiceOver is enabled.
- [binding](binding.md)
  Associates information in a data item with an element.
- [handlesOverflow](handlesoverflow.md)
  Adds the “MORE” label to a description.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [showsScrollIndicator](showsscrollindicator.md)
  Shows a scroll indicator along the side of an element appropriate for the user’s specified language.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [decorationLabel](decorationlabel.md)
  Displays text that describes a displayed element.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/description)*