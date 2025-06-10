# tv-scrollable-bounds-inset

**Framework**: TVML

Creates an unscrollable region of a specified size at the top and bottom of the stack template.

#### Overview

Use the `tv-scrollable-bounds-inset` style to create an unscrollable region of specified size from the top and bottom of the `stackTemplate`. When you use unscrollable regions, the content offset is no longer automatically adjusted to allow “peeking” — the partial view of elements directly above and below the focused element.

Once focus is shifted from an unscrollable region to a scrollable region, the content offset of the template is adjusted to the specified `tv-scrollable-bounds-inset` value, so that the unscrollable region doesn’t appear on screen.

> **Note**: By default, the entire template is scrollable if you don’t define the tv-scrollable-bounds-inset style.

Here’s an example that sets the inset (unscrollable space) at the top, right, bottom, and left all to 100 points.

```xml
<stackTemplate style="tv-scrollable-bounds-inset: 100.0;">
    <banner>
        …
    </banner>
    <collectionList>
        <shelf>
            <section>
                <lockup>…</lockup>
            </section>
        </shelf>
    </collectionList>
</stackTemplate>
```

Here’s an example that sets the inset (unscrollable space) at the top to 50 points, and the inset at the bottom to 75 points.

```xml
<stackTemplate style="tv-scrollable-bounds-inset: 50.0 0.0 75.0 0.0;">
    <banner>
        …
    </banner>
    <collectionList>
        <shelf>
            <section>
                <lockup>…</lockup>
            </section>
        </shelf>
    </collectionList>
</stackTemplate>
```

##### Values for Tv Scrollable Bounds Inset

> ❗ **Important**: Currently, creating unscrollable regions at the left and right of the `stackTemplate `is not supported and will not have any effect.

##### Elements That Use Tv Scrollable Bounds Inset

- [`stackTemplate`](stacktemplate.md)

## Topics

### Specifying Inset Location
- [tv-scrollable-bounds-inset-top](tv-scrollable-bounds-inset-top.md)
  Specifies the size of an unscrollable region only at the top of the stack template.
- [tv-scrollable-bounds-inset-bottom](tv-scrollable-bounds-inset-bottom.md)
  Specifies the size of an unscrollable region only at the bottom of the stack template.

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
- [tv-transition](tv-transition.md)
  Specifies how an element transitions on and off the screen.
- [tv-text-highlight-style](tv-text-highlight-style.md)
  Specifies how an element looks when it comes into focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/tv-scrollable-bounds-inset)*