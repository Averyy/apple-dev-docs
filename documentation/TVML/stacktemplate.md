# stackTemplate

**Framework**: Tvml

Displays groups of products.

#### Overview

Use the `stackTemplate` element to display, for example, displaying different genres of movies. Each group of products is displayed directly underneath the previous group. Products can be displayed in different ways using `carousel`, `grid`, and `shelf` elements. The following figure shows the basic layout for a `stackTemplate` page. The theme for the stack template defaults to the system preference.

![Layout diagram showing a banner area at the top of the screen, and a collection list area containing two shelf areas directly below.](https://docs-assets.developer.apple.com/published/0557616c56247b507d9851899127cbcb/stacktemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `stackTemplate` element in TVML format.

```xml
<stackTemplate>
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

> **Note**: The `shelf` element can be replaced with a `grid` or `carousel` element to change the way products are displayed.

###### Element Descriptions

##### Example

The following listing shows the TVML for a `stackTemplate` example:

```xml
<document>
    <stackTemplate>
        <banner>
            <title>Available Action Movies</title>
        </banner>
        <collectionList>
            <shelf>
                <section>
                    <lockup>
                        <img src="path to images on your server/Car_Movie_250x375_A.png" width="182" height="274" />
                        <title>Movie 1</title>
                    </lockup>
                    <lockup>
                        <img src="path to images on your server/Car_Movie_250x375_B.png" width="182" height="274" />
                        <title>Movie 2</title>
                    </lockup>
                    <lockup>
                        <img src="path to images on your server/Car_Movie_250x375_C.png" width="182" height="274" />
                        <title>Movie 3</title>
                    </lockup>
                </section>
            </shelf>
            <shelf>
                <section>
                    <lockup>
                        <img src="path to images on your servers/Space_Movie/Space_Movie_250x375_B.png" width="182" height="274"></img>
                        <title>Movie 4</title>
                    </lockup>
                    <lockup>
                        <img src="path to images on your server/Space_Movie/Space_Movie_250x375_A.png" width="182" height="274"></img>
                        <title>Movie 5</title>
                    </lockup>
                    <lockup>
                        <img src="path to images on your server/Space_Movie/Space_Movie_250x375_C.png" width="182" height="274"></img>
                        <title>Movie 6</title>
                    </lockup>
                </section>
            </shelf>
        </collectionList>
    </stackTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing two shelves of movie posters.](https://docs-assets.developer.apple.com/published/130cfc10bfca9e7e88f56d8a5be39b4f/stacktemplate-2%402x.png)

You can also customize the stack template’s background content. To do so, embed a `mediaContent `element in a `background `element, as shown in this example:

```xml
<background>
    <mediaContent playbackMode="always">
        <img src="path to images on your server/Car_Movie.png"/>
    </mediaContent>
</background>
```

When you add a video in the background, playback starts 5 seconds after the page is loaded. The video does not repeat.

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [itemID](itemid.md)
  Mark elements for reuse during DOM updates.
- [layoutDirection](layoutdirection.md)
  Specifies the direction in which text is displayed.
- [needsMoreThreshold](needsmorethreshold.md)
  Sets the amount of remaining screen lengths before firing the needs more event.
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

*[View on Apple Developer](https://developer.apple.com/documentation/TVML/stacktemplate)*