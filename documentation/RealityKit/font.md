# font

**Framework**: RealityKit

An array of font names.

#### Overview

The runtime scans this list in ascending order and chooses the first font that the runtime can provide. Font names provide the font family, then the font style, such as “Gill Sans.” You can reference font names using Font Book on macOS.

If the system doesn’t support your chosen font, you can fall back to a generic font by providing one or more generic font specifiers at the end of the font list: `serif`, `san-serif`, `monospaced`, or `cursive`.

##### Declaration

```other
string[] font
```

## See Also

- [content](content.md)
  The characters that the text displays.
- [pointSize](pointsize.md)
  The size of the text’s font.
- [width](width.md)
  The width of the text’s bounding box.
- [height](height.md)
  The height of the text’s bounding box.
- [depth](depth.md)
  A value that defines the depth, in scene units, of the text’s extrusion.
- [wrapMode](wrapmode.md)
  An option that determines the flow of the text.
- [horizontalAlignment](horizontalalignment.md)
  An option that controls the text’s horizontal placement within its bounding box.
- [verticalAlignment](verticalalignment.md)
  An option that controls the text’s vertical placement within its bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/font)*