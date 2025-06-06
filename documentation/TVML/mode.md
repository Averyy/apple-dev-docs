# mode

**Framework**: TVML

Specifies how an image is displayed.

#### Overview

Use the `mode` attribute to define how an image is displayed in the `oneupTemplate` and `showcaseTemplate` elements. The `showcaseTemplate` element can only use the `showcase oneup` attribute value. The `oneupTemplate` can only use the `oneup caption` attribute value. Clicking an image alternates between the selected modes. Here’s an example that displays images in `showcaseTemplate` in `showcase` mode:

```xml
<document>
    <showcaseTemplate mode="showcase">
        <background>
            <img src="path to images on your server/Car_Movie_1920x1080.png" />
        </background>
        <banner>
            <title>Scenes</title>
            <row>
                <button>
                    <text>Slideshow</text>
                </button>
                <button>
                    <text>Screensaver</text>
                </button>
            </row>
        </banner>
        <carousel>
            <section>
                <lockup>
                    <img src="path to images on your server/Car_Movie_453x255_C.png" width="453" height="255" />
                    <title>Scene 1</title>
                </lockup>
                <lockup>
                    <img src="path to images on your server/Car_Movie_500x600.png" width="500" height="600" />
                    <title>Scene 2</title>
                </lockup>
            </section>
        </carousel>
    </showcaseTemplate>
</document>
```

##### Values for Mode

##### Elements That Use Mode

- [`oneupTemplate`](oneuptemplate.md)
- [`showcaseTemplate`](showcasetemplate.md)

## See Also

- [aspectFill](aspectfill.md)
  Stretches an image to fill the containing bounding box.
- [contentsMode](contentsmode.md)
  Specifies how an image is expanded to fill its containing element.
- [opaque](opaque.md)
  Indicates whether an image has a transparent background.
- [type](type.md)
  Specifies how a badge is drawn.
- [value](value.md)
  Specifies the value used for a fillable element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/mode)*