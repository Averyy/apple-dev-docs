# paradeTemplate

**Framework**: TVML

Displays a groups of items along one side of a page and scrolling images on the other side.

#### Overview

Use the `paradeTemplate` element to display a list of automatically scrolling, static images on the left that are associated with a selected image category on the right. For example, a user selects Action movies, and the associated images automatically start scrolling. The following figure shows the basic layout for a `paradeTemplate` page. The theme for the parade template defaults to the system preference.

![Layout diagram showing an image deck area on the left side, and a header area above a section area on the right.](https://docs-assets.developer.apple.com/published/f01bc2bef885528f38f9ea752d3af9fe/paradetemplate-1%402x.png)

##### Main Elements

The following listing shows main elements of the `paradeTemplate` in TVML format.

```xml
<paradeTemplate>
   <list>
      <header>
         <title>Title</title>
      </header>
      <section>
         <listItemLockup>
            <title>Title 1</title>
         </listItemLockup>
         <listItemLockup>
            <title>Title 2</title>
         </listItemLockup>
      </section>
      <relatedContent>
         <imgDeck>
            <img src="" />
            <img src="" />
         </imgDeck>
      </relatedContent
   </list>
</paradeTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `paradeTemplate` example.

```xml
<document>
    <paradeTemplate>
        <list>
            <header>
                <title>Movie Genres</title>
            </header>
            <section>
                <listItemLockup>
                    <title>Action</title>
                </listItemLockup>
                <listItemLockup>
                    <title>Comedy</title>
                </listItemLockup>
                <listItemLockup>
                    <title>Horror</title>
                </listItemLockup>
                <listItemLockup>
                    <title>Kids</title>
                </listItemLockup>
                <listItemLockup>
                    <title>Drama</title>
                </listItemLockup>
            </section>
            <relatedContent>
                <imgDeck>
                    <img src="path to images on your server/Car_Movie_250x375.png "/>
                    <img src="path to images on your server/Car_Movie_250x375_A.png "/>
                    <img src="path to images on your server/Car_Movie_250x375_B.png "/>
                    <img src="path to images on your server/Car_Movie_250x375_C.png "/>
                </imgDeck>
            </relatedContent>
        </list>
    </paradeTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing movie genres on the right. A collage of images relating to the selected movie genre is on the left.](https://docs-assets.developer.apple.com/published/253b680d735eb3db54000a0bc059cd02/paradetemplate-2%402x.png)

## Topics

### Valid TVML Attributes
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
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
- [mainTemplate](maintemplate.md)
  Displays user options for a media item.
- [menuBarTemplate](menubartemplate.md)
  Creates a page with items along the top and related information below.
- [oneupTemplate](oneuptemplate.md)
  Creates a page that allows users to navigate between full-screen images.
- [productBundleTemplate](productbundletemplate.md)
  Displays information for a group of related media items.
- [productTemplate](producttemplate.md)
  Displays detailed information about a single product.
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/paradetemplate)*