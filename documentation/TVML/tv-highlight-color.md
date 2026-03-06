# tv-highlight-color

**Framework**: TVML

Changes an element’s color when it comes into focus.

#### Overview

Here’s an example of how to change a button’s text color when the button comes into focus.

```xml
<button>
   <text style="tv-highlight-color:rgb(0,0,255,0.3)">Push me</text>
</button>
```

##### Values for Tv Highlight Color

- **`rgb(r,g,b)`**: The background color of an element, where `r,g,b` are the red, green, and blue color components, and have a value range from `0-255`.
- **`rgba(r,g,b,a)`**: The background color of an element, where `r,g,b` are the red, green, and blue color components, and have a value range from `0-255`, and `a` is the alpha applied to the color, ranging from `0.0-1.0`.
- **`transparent`**: The background color of the element, which is transparent.

##### Elements That Use Tv Highlight Color

- [`badge`](badge.md)
- [`decorationLabel`](decorationlabel.md)
- [`description`](description.md)
- [`listItemLockup`](listitemlockup.md)
- [`menuItem`](menuitem.md)
- [`ordinal`](ordinal.md)
- [`ratingCard`](ratingcard.md)
- [`reviewCard`](reviewcard.md)
- [`segmentBar`](segmentbar.md)
- [`subtitle`](subtitle.md)
- [`text`](text.md)
- [`title`](title.md)

## See Also

- [background-color](background-color.md)
  Changes the background color of an element.
- [color](color.md)
  Changes the color of an element.
- [tv-tint-color](tv-tint-color.md)
  Sets the tint color for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/tv-highlight-color)*