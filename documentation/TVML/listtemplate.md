# listTemplate

**Framework**: TVML

Displays a list of items along one side of a page and the corresponding image on the other side.

#### Overview

Use the `listTemplate` element to display a list of items; for example, a list of the user’s favorite movies. Whereas you use the catalog template to display categories of a product (action movies, comedies, favorite movies), you use the list template to display actual contents of one category, such as a list of the user’s favorite movies. The items are listed on the right side of the screen with like items grouped together in a section. A title providing a brief description of the items is contained in a header area directly above the listed items. When an item is selected, information about the item is displayed on the left side of the screen. The following figure shows the basic layout for a `listTemplate` page. The theme for the list template defaults to the system preference.

![Layout diagram showing a banner area at the top, header and section areas on the right, and a related content area on the left.](https://docs-assets.developer.apple.com/published/78e33d9dce40fd1682e15869baef0fc5/listtemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `listTemplate` in TVML format.

```xml
<listTemplate>
   <banner>
      …
   </banner>
   <list>
      <header>
         …
      </header>
      <section>
         <listItemLockup>
            <title>…</title>
            <relatedContent>
               …
            </relatedContent>
         </listItemLockup
      </section>
   </list>
</listTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `listTemplate` example. An image and a description that relate to the highlighted item are displayed on the left side of the screen.

```xml
<document>
   <listTemplate>
      <banner>
         <title>Johnny Appleseed's Movie Collection</title>
      </banner>
      <list>
         <header>
            <title>Favorite Movies</title>
         </header>
         <section>
            <listItemLockup>
               <title>Movie 1</title>
               <relatedContent>
                  <lockup>
                     <img src="path to images on your server/Car_Movie_1920x1080.png" width="857" height="482" />
                     <title>Movie 1</title>
                     <description>A brief description for the first movie should go here.</description>
                  </lockup>
               </relatedContent>
            </listItemLockup>
            <listItemLockup>
               <title>Movie 2</title>
               <relatedContent>
                  <lockup>
                     <img src="path to images on your server/Car_Movie_800x600.png" width="857" height="482" />
                     <title>Movie 2</title>
                     <description>A brief description for the second movie should go here.</description>
                  </lockup>
               </relatedContent>
            </listItemLockup>
            <listItemLockup>
               <title>Movie 3</title>
               <relatedContent>
                  <lockup>
                     <img src="path to images on your server/Car_Movie_720x720.png" width="857" height="482" />
                     <title>Movie 3</title>
                     <description>A brief description for the third movie should go here.</description>
                  </lockup>
               </relatedContent>
            </listItemLockup>
         </section>
      </list>
   </listTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing an example of a movie collection. A list of movies is on the right and an image of the selected movie is on the left.](https://docs-assets.developer.apple.com/published/23e1a38fac4fd450c81cb525b885fb6b/listtemplate-2%402x.png)

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
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/listtemplate)*