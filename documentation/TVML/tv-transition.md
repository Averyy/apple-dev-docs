# tv-transition

**Framework**: TVML

Specifies how an element transitions on and off the screen.

#### Overview

Use the `tv-transition` style to apply a transition effect to an element.

##### Values for Tv Transition

- **`dissolve`**: The element stays in place and uses a dissolve effect.
- **`magicMove`**: The element uses the magic move transition. When the user swipes to the left, the current image shrinks slightly, and a new image is brought on top of it from the right. When the user swipes to the right, the image slides off screen to the right. This action reveals the next image, which then grows to fill the screen.
- **`none`**: No transition effect is applied to the element.
- **`push`**: The element is pushed onto the screen.
- **`wipe`**: The element is wiped from the screen.

##### Elements That Use Tv Transition

- [`oneupTemplate`](oneuptemplate.md)

## See Also

- [Color Styles](color-styles.md)
  Provide the ability to customize an element’s color.
- [Text Styles](text-styles.md)
  Change the text characteristics for an element.
- [Element Shaping](element-shaping.md)
  Modify the size and shape of an element.
- [Element Alignment and Spacing](element-alignment-and-spacing.md)
  Modify the alignment and spacing between elements.
- [tv-placeholder](tv-placeholder.md)
  Sets a default image for an `img` or `monogram` element.
- [tv-rating-style](tv-rating-style.md)
  Sets the displayed image for rating a product.
- [tv-text-highlight-style](tv-text-highlight-style.md)
  Specifies how an element looks when it comes into focus.
- [tv-scrollable-bounds-inset](tv-scrollable-bounds-inset.md)
  Creates an unscrollable region of a specified size at the top and bottom of the stack template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/tv-transition)*