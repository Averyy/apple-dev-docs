# Preliminary_Text

**Framework**: RealityKit

A prim that renders 3D text in a scene.

#### Overview

Because `Preliminary_Text` prim is an `Xformable` prim, you define its position either by specifying an offset in world coordinates, or by specifying that the prim should inherit its parent transform.

Alternatively, you can request that the runtime anchor a text prim in the real world by inheriting `Preliminary_AnchoringAPI`. Many AR experiences include anchored text to add information or context about real-world objects or virtual content.

##### Declaration

```other
class Preliminary_Text "Preliminary_Text" (
    inherits = </Gprim>
)
```

##### Create Single Line or Flowing Text

The following example demonstrates single-line text.

```other
def Preliminary_Text "heading"
{
    string content = "Units Sold"
    string[] font = [ "Helvetica", "Arial" ]
    token wrapMode = "singleLine"
    token horizontalAlignment = "left"
    token verticalAlignment = "baseline"
}
```

The following example shows text flowing in a rectangular region, with line breaks as needed.

```other
def Preliminary_Text "sign"
{
    string content = "Now is the time for all good people to come to the aid of their country."
    string[] font = [ "ZapfChancery", "Bradley Hand", "cursive" ]
    token wrapMode = "flowing"
    float width = 120
    float height = 100
    token horizontalAlignment = "center"
    token verticalAlignment = "top"
}
```

## Topics

### Properties
- [content](content.md)
  The characters that the text displays.
- [font](font.md)
  An array of font names.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/preliminary-text)*