# contentsMode

**Framework**: TVML

Specifies how an image is expanded to fill its containing element.

#### Overview

Use the `contentsMode` attribute to specify how the image is scaled within its bounding box. Here’s an example that demonstrates the `contentsMode` attribute in a `stackTemplate`:

```xml
<document>
    <stackTemplate>
        <banner>
            <title>contentsMode</title>
        </banner>
        <collectionList>
            <shelf>
                <section>
                    <lockup>
                        <img contentsMode="aspectFit" width="600" height="300" aspectRatio="1:1" src="path to images on your server/Car_Movie_200x200.png"/>
                        <title>aspectFit</title>
                    </lockup>
                    <lockup>
                        <img contentsMode="aspectFitBB" width="600" height="300" src="path to images on your server/Car_Movie_200x200.png"/>
                        <title>aspectFitBB</title>
                    </lockup>
                    <lockup>
                        <img contentsMode="aspectFill" width="600" height="300" src="path to images on your server/Car_Movie_200x200.png" contentsMode="aspectFill"/>
                        <title>aspectFill</title>
                    </lockup>
                </section>
            </shelf>
        </collectionList>
    </stackTemplate>
</document>
```

> ❗ **Important**: When using the `aspectFit` value, you must also include the [`aspectRatio`](aspectratio.md) attribute for the content to scale appropriately.

When using the `aspectFit` value, you must also include the [`aspectRatio`](aspectratio.md) attribute for the content to scale appropriately.

##### Values

##### Elements That Use Contentsmode

- [`img`](img.md)

## See Also

- [aspectFill](aspectfill.md)
  Stretches an image to fill the containing bounding box.
- [opaque](opaque.md)
  Indicates whether an image has a transparent background.
- [mode](mode.md)
  Specifies how an image is displayed.
- [type](type.md)
  Specifies how a badge is drawn.
- [value](value.md)
  Specifies the value used for a fillable element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/contentsmode)*