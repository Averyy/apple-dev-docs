# productTemplate

**Framework**: Tvml

Displays detailed information about a single product.

#### Overview

Use the `productTemplate` element to display, for example, a page that describes a movie, including information about the actors, ratings, and like movies. The page displays general information about the product in the top two-thirds of the screen with a row of related products directly below. A user can scroll down and access detailed information about the product, including critical reviews, actor biographies, and information about any included extras.

The following figure shows the basic layout for a `productTemplate` page. The default theme for a product template is `dark` when a background image is specified; otherwise, the product template defaults to the system preference.

![Layout diagram showing an info list area on the left side of the screen, a stack area in the middle, and a banner area on the right. A shelf area is at the bottom of the screen. A second shelf area is shown as being off the bottom of the screen.](https://docs-assets.developer.apple.com/published/46f99b3cc92265c2e5599363d7aa07d2/producttemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the productTemplate element in TVML format.

```xml
<productTemplate>
    <banner>
        <infoList>
        </infoList>
        <stack>
            <title>…</title>
            <subtitle>…</subtitle>
            <row>
            </row>
            <description>…</description>
            <buttonLockup>
            </buttonLockup>
        </stack>
        <heroImage src="…" />
    </banner>
    <shelf>
    </shelf>
    <!—- Everything following is under the fold —->
        <shelf>
        </shelf>
        <productInfo>
        </productInfo>
    </productTemplate>
```

> **Note**: You can change the look of a `productTemplate` page by removing `heroImage` from the `stack` element and replacing it with an `img` element that covers the entire screen.

###### Element Descriptions

##### Example

The following listing shows the TVML for a `productTemplate` example:

```xml
<document>
   <productTemplate>
      <background>
      </background>
      <banner>
         <infoList>
            <info>
               <header>
                  <title>Director</title>
               </header>
               <text>John Appleseed</text>
            </info>
            <info>
               <header>
                  <title>Actors</title>
               </header>
               <text>Anne Johnson</text>
               <text>Tom Clark</text>
               <text>Maria Ruiz</text>
            </info>
         </infoList>
         <stack>
            <title>WWDC Road Trip</title>
            <row>
               <text><badge src="resource://tomato-fresh"/> 99%</text>
               <text>1hr 54min</text>
               <text>Comedy</text>
               <text>2015</text>
               <badge src="resource://mpaa-pg" class="badge" />
               <badge src="resource://cc" class="badge" />
            </row>
            <description handlesOverflow ="true">An aspiring developer gets a ticket to WWDC at the last minute. Now they need to get across country in time for the keynote, and the only person who can help is their quirky roommate.</description>
            <text>Language information can go here</text>
            <row>
               <buttonLockup>
                  <badge src="resource://button-preview" />
                  <title>Preview</title>
               </buttonLockup>
               <buttonLockup type="buy">
                  <text>$9.99</text>
                  <title>Buy</title>
               </buttonLockup>
            </row>
         </stack>
         <heroImg src="path to images on your server/Car_Movie_720x1080.png" />
      </banner>
      <shelf>
         <header>
            <title>Viewers Also Watched</title>
         </header>
         <section>
            <lockup>
               <img src="path to images on your server/Car_Movie_250x375_A.png" width="150" height="226" />
               <title>Turn</title>
            </lockup>
            <lockup>
               <img src="path to images on your server/Car_Movie_250x375_B.png" width="150" height="226" />
               <title>Road</title>
            </lockup>
            <lockup>
               <img src="path to images on your server/Car_Movie_250x375_C.png" width="150" height="226" />
               <title>Helicopter</title>
            </lockup>
         </section>
      </shelf>
<!—- Everything past this is below the fold —->
      <shelf>
         <header>
            <title>Reviews and Ratings</title>
         </header>
         <section>
            <ratingCard>
               <title>4.1 / 5</title>
               <ratingBadge value="0.7"></ratingBadge>
               <description>Average of 2,241 iTunes user ratings and reviews.</description>
            </ratingCard>
            <ratingCard>
               <title><badge src="resource://tomato-fresh" /> 99%</title>
               <text>Tomatometer</text>
               <infoTable>
                  <info>
                     <header>
                        <title>175</title>
                     </header>
                     <text>Reviews</text>
                  </info>
                  <info>
                     <header>
                        <title>173</title>
                     </header>
                     <text>Fresh</text>
                  </info>
                  <info>
                     <header>
                        <title>2</title>
                     </header>
                     <text>Rotten</text>
                  </info>
               </infoTable>
            </ratingCard>
            <reviewCard>
               <badge src="resource://tomato-fresh-m" />
               <title>WWDC Review</title>
               <description>Brief review here</description>
               <text>Ravi Patel June, 8 2015</text>
            </reviewCard>
         </section>
      </shelf>
      <shelf>
         <header>
            <title>Cast and Crew</title>
         </header>
         <section>
            <monogramLockup>
               <monogram firstName="Anne" lastName="Johnson"/>
               <title>Anne Johnson</title>
               <subtitle>Actor</subtitle>
            </monogramLockup>
            <monogramLockup>
               <monogram firstName="Tom" lastName="Clark"/>
               <title>Tom Clark</title>
               <subtitle>Actor</subtitle>
            </monogramLockup>
            <monogramLockup>
               <monogram firstName="Maria" lastName="Ruiz"/>
               <title>Maria Ruiz</title>
               <subtitle>Actor</subtitle>
            </monogramLockup>
         </section>
      </shelf>
      <productInfo>
         <infoTable>
            <header>
               <title>Information</title>
            </header>
            <info>
               <header>
                  <title>Studio</title>
               </header>
               <text>Apple</text>
            </info>
            <info>
               <header>
                  <title>Runtime</title>
               </header>
               <text>1:54</text>
            </info>
            <info>
               <header>
                  <title>Format</title>
               </header>
               <text>Widescreen</text>
            </info>
         </infoTable>
         <infoTable>
            <header>
               <title>Languages</title>
            </header>
            <info>
               <header>
                  <title>Primary</title>
               </header>
               <text>English (Dolby 5.1), Subtitles, CC</text>
            </info>
            <info>
               <header>
                  <title>Additional</title>
               </header>
               <text>Cantonese (Subtitles)</text>
            </info>
         </infoTable>
         <infoTable style="tv-line-spacing:10;">
            <header>
               <title>Accessibility</title>
            </header>
            <info>
               <header>
                  <textBadge>SDH</textBadge>
               </header>
               <text>Subtitles for the deaf and Hard of Hearing (SDH) refer to subtitles in the original lanuage with the addition of relevant non-dialog information.</text>
            </info>
         </infoTable>
      </productInfo>
   </productTemplate>
</document>
```

The following figures show the ouput for the above example. The first figure shows the output for the example when it first appears on screen. The second figure shows the output below the fold as the user scrolls down the screen.

![Screenshot showing a sample product. Director and actor information is on the left, a description in the middle, and an image of the product on the right. A row of similar movies is at the bottom.](https://docs-assets.developer.apple.com/published/1eca8755bdd44573b05e2b9195c1fa8d/producttemplate-2%402x.png)

![Screenshot showing the second page of the product. The top row contains review and ratings, the middle row contains actor information, and the bottom row contains general information about the product.](https://docs-assets.developer.apple.com/published/8589c672ed9f410b02f2c2172057aec2/producttemplate-3%402x.png)

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
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVML/producttemplate)*