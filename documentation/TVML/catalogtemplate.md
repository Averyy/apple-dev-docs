# catalogTemplate

**Framework**: TVML

Displays groups of items along one side of a page and images of a group’s contents on the other side.

#### Overview

Use the `catalogTemplate` element to display information about groups of like products; for example, a movie catalog that provides categories for dramas, comedies, and all movies. Each group of products is contained in its own section and displayed along the left side of the screen. Images depicting the products contained within a selected group are displayed in the related content area on the right side of the screen. The following figure shows the basic layout for a `catalogTemplate` page. The theme for the catalog template defaults to the system preference.

![Layout diagram showing a banner area at the top, three section areas on the left side, and a related content area on the right.](https://docs-assets.developer.apple.com/published/3b0561b7d68246033f994c5c57b3c948/catalogtemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `catalogTemplate` element in TVML format.

```xml
<catalogTemplate>
   <banner>
      <title>…</title>
   </banner>
   <list>
      <section>
         <listItemLockup>
            …
         </listItemLockup>
      </section>
      <section>
         <header>
            …
         </header>
         <listItemLockup>
            …
         </listItemLockup>
      </section>
   </list>
</catalogTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `catalogTemplate` example. The example displays a title along the top of the screen. Two items representing movie categories, All Movies and Comedies, are listed along the left side of the screen. Movie posters are presented on the right in a grid format according to which movie category the user selects.

```xml
<document>
   <catalogTemplate>
      <banner>
         <title>Movies</title>
      </banner>
      <list>
         <section>
            <listItemLockup>
               <title>All Movies</title>
               <decorationLabel>6</decorationLabel>
               <relatedContent>
                  <grid>
                     <section>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375_A.png" width="250" height="376" />
                           <title>Movie 1</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375_B.png" width="250" height="376" />
                           <title>Movie 2</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375_C.png" width="250" height="376" />
                           <title>Movie 3</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375.png" width="250" height="376" />
                           <title>Movie 4</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375_C.png" width="250" height="376" />
                           <title>Movie 5</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375.png" width="250" height="376" />
                           <title>Movie 6</title>
                        </lockup>
                     </section>
                  </grid>
               </relatedContent>
            </listItemLockup>
            <listItemLockup>
               <title>Comedies</title>
               <decorationLabel>4</decorationLabel>
               <relatedContent>
                  <grid>
                     <section>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375_B.png" width="250" height="376" />
                           <title>Movie 2</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375_A.png" width="250" height="376" />
                           <title>Movie 1</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375.png" width="250" height="376" />
                           <title>Movie 4</title>
                        </lockup>
                        <lockup>
                           <img src="path to images on your server/Car_Movie_250x375_C.png" width="250" height="376" />
                           <title>Movie 3</title>
                        </lockup>
                     </section>
                  </grid>
               </relatedContent>
            </listItemLockup>
         </section>
      </list>
   </catalogTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing several movie posters on the right and a list of movie categories on the left.](https://docs-assets.developer.apple.com/published/c65085b7852b69f01e7b241b3a1d7f53/catalogtemplate-2%402x.png)

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
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/catalogtemplate)*