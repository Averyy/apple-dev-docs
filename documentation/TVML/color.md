# color

**Framework**: TVML

Changes the color of an element.

#### Overview

Use the `color` style to change the color an an element. Here’s an example of how to change the text color inside of a `description` element.

```xml
<description style="color:rgb(0,0,255,0.3)">Light purple</description>
```

##### Values for Color

- **`rgb(r,g,b)`**: The background color of an element, where `r,g,b` are the red, green, and blue color components, and have a value range from `0-255`.
- **`rgba(r,g,b,a)`**: The background color of an element, where `r,g,b` are the red, green, and blue color components, and have a value range from `0-255`, and `a` is the alpha applied to the color, ranging from `0.0-1.0`.
- **`transparent`**: The background color of the element is transparent.

##### Elements That Use Color

- [`decorationLabel`](decorationlabel.md)
- [`description`](description.md)
- [`ordinal`](ordinal.md)
- [`segmentBar`](segmentbar.md)
- [`subtitle`](subtitle.md)
- [`text`](text.md)
- [`textBadge`](textbadge.md)
- [`title`](title.md)

## See Also

- [background-color](background-color.md)
  Changes the background color of an element.
- [tv-highlight-color](tv-highlight-color.md)
  Changes an element’s color when it comes into focus.
- [tv-tint-color](tv-tint-color.md)
  Sets the tint color for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/color)*