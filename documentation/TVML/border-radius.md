# border-radius

**Framework**: TVML

Changes the shape of an element’s corner.

#### Overview

Use the `border-radius` style to apply rounded corners to elements. Here’s an example that changes the border radius of an `img` element.

```xml
<lockup>
   <img style="border-radius:12" src="path to image" width="250" height="376" />
   <title>Movie 1</title>
</lockup>
```

##### Values for Border Radius

There are four ways to designate the border-radius style as a 4-tuple:

- `border-radius: X1 X2 X3 X4`—Where X1 is applied to the top-left corner, X2 is applied to the top-right corner, X3 is applied to the bottom-right corner, and X4 is applied to the bottom-left corner.
- `border-radius: X1 X2 X3`—Where X1 is applied to the top-left corner, X2 is applied to the top-right and bottom-left corners, and X3 is applied to the bottom-right corner.
- `border-radius: X1 X2`—Where X1 is applied to the top-left and bottom-right corners, and X2 is applied to the top-right and bottom-left corners.
- `border-radius: X1`—Where X1 is applied to each corner.

##### Elements That Use Border Radius

- [`card`](card.md)
- [`heroImg`](heroimg.md)
- [`img`](img.md)
- [`monogram`](monogram.md)
- [`ratingCard`](ratingcard.md)
- [`reviewCard`](reviewcard.md)
- [`textBadge`](textbadge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/border-radius)*