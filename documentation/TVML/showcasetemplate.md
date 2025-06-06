# showcaseTemplate

**Framework**: TVML

Displays images the user can navigate between.

#### Overview

Use the `showcaseTemplate` element to display a row of images with descriptions associated with each image; for example, displaying a set of screenshots to promote a movie. Users can scroll between images. When an image comes into focus, the size of the image is increased to be slightly larger than the other images. The following figure shows the basic layout for a showcaseTemplate page. The default theme for a showcase template is `dark`.

![Layout diagram showing a banner area in the upper-right corner of the screen, and three lockup areas below.](https://docs-assets.developer.apple.com/published/5ba462da04d20bd14fcafa08d9d88189/showcasetemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `showcaseTemplate` element in TVML format.

```xml
<showcaseTemplate>
    <background>…</background>
    <banner>
        <title>…</title>
        <row>
            <button>…</button>
        </row>
    </banner>
    <carousel>
        <section>
            <lockup>…</lockup>
        </section>
    </carousel>
</showcaseTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `showcaseTemplate` example.

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
                <lockup>
                    <img src="path to images on your server/Car_Movie_308x308_B.png" width="308" height="308" />
                    <title>Scene 3</title>
                </lockup>
                <lockup>
                    <img src="path to images on your server/Car_Movie_800x600.png" width="800" height="600" />
                    <title>Scene 4</title>
                </lockup>
            </section>
        </carousel>
    </showcaseTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a title and user options at the top of the screen, and three images evenly spaced in the middle of the screen.](https://docs-assets.developer.apple.com/published/4b4fcd434dd85e135e21ddab3f8161d5/showcasetemplate-2%402x.png)

## Topics

### Valid TVML Attributes
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
- [binding](binding.md)
  Associates information in a data item with an element.
- [layoutDirection](layoutdirection.md)
  Specifies the direction in which text is displayed.
- [mode](mode.md)
  Specifies how an image is displayed.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [alertTemplate](alerttemplate.md)
  Displays important information to the user.
- [catalogTemplate](catalogtemplate.md)
  Displays groups of items along one side of a page and images of a group’s contents on the other side.
- [compilationTemplate](compilationtemplate.md)
  Displays information about a single media item and its components.
- [descriptiveAlertTemplate](descriptivealerttemplate.md)
  Displays large amounts of important information to the user.
- [divTemplate](divtemplate.md)
  Provides the ability to create pages that don’t conform to a layout defined by another template.
- [formTemplate](formtemplate.md)
  Provides the ability to gather information from the user.
- [listTemplate](listtemplate.md)
  Displays a list of items along one side of a page and the corresponding image on the other side.
- [loadingTemplate](loadingtemplate.md)
  Displays a spinner and description on the screen.
- [mainTemplate](maintemplate.md)
  Displays user options for a media item.
- [menuBarTemplate](menubartemplate.md)
  Creates a page with items along the top and related information below.
- [oneupTemplate](oneuptemplate.md)
  Creates a page that allows users to navigate between full-screen images.
- [paradeTemplate](paradetemplate.md)
  Displays a groups of items along one side of a page and scrolling images on the other side.
- [productBundleTemplate](productbundletemplate.md)
  Displays information for a group of related media items.
- [productTemplate](producttemplate.md)
  Displays detailed information about a single product.
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/showcasetemplate)*