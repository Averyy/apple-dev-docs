# searchTemplate

**Framework**: TVML

Searches for a media item based on user input.

#### Overview

Use the `searchTemplate` element to display a text field that takes user input in order to search for a specific item; for example, looking for a specific movie to download. Developers can also display preselected results in a `shelf`, `list`, or `collectionList` element under the search field. The following figure shows the basic layout for a `searchTemplate` page. The theme for the search template defaults to the system preference.

![Layout diagram showing a search field at the top, a keyboard area directly below, and a large area for search results at the bottom.](https://docs-assets.developer.apple.com/published/961a6394b691c143bea3c091f1f364fd/searchtemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `searchTemplate` element in TVML format.

```xml
<searchTemplate>
    <searchField />
    <shelf>
        <header>
            …
        </header>
        <section>
            <lockup>
                <img />
                <title>…</title>
            </lockup>
        </section>
    </shelf>
</searchTemplate>
```

> **Note**: The `shelf` element can be replaced with a `collectionList` or `list` element to change the look of the search results.

The `shelf` element can be replaced with a `collectionList` or `list` element to change the look of the search results.

###### Element Descriptions

##### Example

The following listing shows the TVML for a `searchTemplate` example. The example displays a search field and keyboard along the top of the screen. A shelf is prepopulated with popular movies. Modify your main JavaScript file to accept the user input from the search field. For more information on available JavaScript functions, see [`TVMLKit JS`](https://developer.apple.com/documentation/tvmljs).

```xml
<document>
    <searchTemplate>
        <searchField/>
        <shelf>
            <header>
                <title>Popular</title>
            </header>
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
    </searchTemplate>
</document>
```

The following listing shows the output for the above example:

![Screenshot showing a search field at the top of the screen and three movies at the bottom.](https://docs-assets.developer.apple.com/published/b2d096819f273e48e28d379bf322dc60/searchtemplate-2%402x.png)

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [itemID](itemid.md)
  Mark elements for reuse during DOM updates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/searchtemplate)*