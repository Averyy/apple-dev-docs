# mainTemplate

**Framework**: TVML

Displays user options for a media item.

#### Overview

Use the `mainTemplate` element to display options to the user; for example, the main page for a movie with options to play the movie, see extra content, and jump to specific scenes. The background area contains an image relating to the product, and the options are contained in a menu bar along the bottom of the screen. The following figure shows the basic layout for a `mainTemplate` page. The default theme for a main template is `dark`.

![Layout diagram showing a large background area with a menu bar at the bottom.](https://docs-assets.developer.apple.com/published/8a33f330c11beb223b8cfadc7410f918/maintemplate-1%402x.png)

##### Main Elements

The following listing shows the elements of the mainTemplate element in TVML format.

```xml
<mainTemplate>
    <background>…</background>
    <menuBar>
        <section>
            <menuItem>…</menuItem>
            <menuItem>…</menuItem>
        </section>
    </menuBar>
</mainTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `mainTemplate` example. The example displays a full-screen image as the background. A menu bar contains three navigable options.

```xml
<document>
    <mainTemplate>
        <background>
            <img src="path to images on your server/Car_Movie_1920x1080" />
        </background>
        <menuBar>
            <section>
                <menuItem>
                    <title>PLAY</title>
                </menuItem>
                <menuItem>
                    <title>SCENES</title>
                </menuItem>
                <menuItem>
                    <title>EXTRAS</title>
                </menuItem>
            </section>
        </menuBar>
    </mainTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a stylized city landscape. A menu bar showing user options is along the bottom.](https://docs-assets.developer.apple.com/published/7e026ecb08d19f44c59df2307acb6aab/maintemplate-2%402x.png)

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [layoutDirection](layoutdirection.md)
  Specifies the direction in which text is displayed.
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
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/maintemplate)*