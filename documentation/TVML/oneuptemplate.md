# oneupTemplate

**Framework**: TVML

Creates a page that allows users to navigate between full-screen images.

#### Overview

Use the `oneupTemplate` element to display a single, full-screen image. Users can navigate left or right on the remote to select another image. Activating an up action on the remote will shrink the image and allow a description to be displayed. The following figure shows the basic layout for a `oneupTemplate` page. The default theme for a oneup template is `dark`.

![Layout diagram showing a large image area, and a title area followed by a row area at the bottom.](https://docs-assets.developer.apple.com/published/85fb320ae5f70c9902bd68c48e4fe5fc/oneuptemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `oneupTemplate` element in TVML format.

```xml
<oneupTemplate>
    <section>
        <lockup>
            <img />
            <title>…</title>
            <row>
                …
            </row>
        </lockup>
        <lockup>
            …
        </lockup>
    </section>
</oneupTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `oneupTemplate` example. The example shows a full screen image, with information about the image displayed along the bottom of the screen when the user zooms into the image.

```xml
<document>
    <oneupTemplate mode="oneup caption" handlesOverflow="true">
        <section>
            <lockup>
                <img src="path to images on your server/Car_Movie_1920x1080.png" />
                <title>WWDC Roadtrip</title>
                <row>
                    <subtitle>San Francisco</subtitle>
                    <subtitle>June 8, 2015</subtitle>
                </row>
            </lockup>
            <lockup>
                <img src="path to images on your server/Beach_Movie_1920x1080.png" />
                <title>Beach time</title>
                <row>
                    <subtitle>Santa Cruz</subtitle>
                    <subtitle>May 1, 2015</subtitle>
                </row>
            </lockup>
            <lockup>
                <img src="path to images on your server/Space_Movie_1920x1080.png" />
                <title>Spaced out</title>
                <row>
                    <subtitle>Space station</subtitle>
                    <subtitle>July 15, 2015</subtitle>
                </row>
            </lockup>
        </section>
    </oneupTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a stylized landscape. A title is directly below the image.](https://docs-assets.developer.apple.com/published/ffe7264ef609c4e3b073daa62a4c0c07/oneuptemplate-2%402x.png)

## Topics

### Valid TVML Styles
- [tv-transition](tv-transition.md)
  Specifies how an element transitions on and off the screen.
### Valid TVML Attributes
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
- [paradeTemplate](paradetemplate.md)
  Displays a groups of items along one side of a page and scrolling images on the other side.
- [productBundleTemplate](productbundletemplate.md)
  Displays information for a group of related media items.
- [productTemplate](producttemplate.md)
  Displays detailed information about a single product.
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/oneuptemplate)*