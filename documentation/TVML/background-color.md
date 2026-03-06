# background-color

**Framework**: TVML

Changes the background color of an element.

#### Overview

Here’s an example of how to change the background color of a `description` element.

```xml
<description style="background-color:rgba(0,0,255,0.3)">Light purple background</description>
```

##### Values for Background Color

- **`rgb(r,g,b)`**: The background color of an element, where `r,g,b` are the red, green, and blue color components, and have a value range from `0-255`.
- **`rgba(r,g,b,a)`**: The background color of an element, where `r,g,b` are the red, green, and blue color components, and have a value range from `0-255`, and `a` is the alpha applied to the color, ranging from `0.0-1.0`.
- **`transparent`**: The background color of the element, which is transparent.

##### Elements That Use Background Color

- [`description`](description.md)
- [`ratingCard`](ratingcard.md)
- [`reviewCard`](reviewcard.md)
- [`textBadge`](textbadge.md)

## See Also

- [color](color.md)
  Changes the color of an element.
- [tv-highlight-color](tv-highlight-color.md)
  Changes an element’s color when it comes into focus.
- [tv-tint-color](tv-tint-color.md)
  Sets the tint color for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/background-color)*