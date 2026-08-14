# productBundleTemplate

**Framework**: TVML

Displays information for a group of related media items.

#### Overview

Use the `productBundleTemplate` element to display detailed information about a product bundle, such as a page that describes a television series, including information about the actors, ratings, and series episodes. The top two-thirds of the screen displays general information about the product. The shelf at the bottom provides a row of related items, such as episodes of the show. A user can scroll down and access detailed information about the product, such as critical reviews, actor biographies, and information about any included extras.

The default theme for a product bundle template is `dark` when you specify a background image; otherwise, the product bundle template defaults to the system preference. You can also change the look of a `productBundleTemplate` page by removing `heroImage` from the `stack` element and replacing it with an `img` element that covers the entire screen.

The following figure shows the basic layout for a `productBundleTemplate` page.

![Layout diagram showing a stack area on the left side of the screen and a banner area on the right. A shelf area is at the bottom of the screen. A second shelf area is shown as being off the bottom of the screen.](/images/com.apple.TVML/productbundletemplate-1@2x.png)

##### Main Elements

The following listing shows the main elements of the `productBundleTemplate` element in TVML format.

```xml
<document>
    <productBundleTemplate>
        <background>
        </background>
        <banner>
            <stack>
                <title>…</title>
                <row>
                </row>
                <text>…</text>
                <description>…</description>
                <row>
                    <buttonLockup>
                    </buttonLockup>
                </row>
            </stack>
            <heroImg src="…" />
        </banner>
        <shelf>
        </shelf>
        !— Everything following is under the fold —>
        <shelf>
        </shelf>
        <productInfo>
            …
        </productInfo>
    </productBundleTemplate>
</document>
```

###### Element Descriptions

- **[`background`](background.md)**: Images or audio to be presented in the background.
- **[`banner`](banner.md)**: Element containing various elements that provide primary information about the product, such as a TV show title and episode title, description, and buttons for purchasing or previewing.
- **[`buttonLockup`](buttonlockup.md)**: A type of button that can contain an image (the `badge` element) as well as text.
- **[`description`](description.md)**: The text that describes the show.
- **[`heroImg`](heroimg.md)**: An image of the show.
- **[`productInfo`](productinfo.md)**: Technical information about the product bundle, such as a show’s runtime, language availability, and accessibility information.
- **[`row`](row.md)**: A group of information elements.
- **[`shelf`](shelf.md)**: An element containing row elements. Several shelves are used to display information like shows other users have watched and extra features provided by this product.
- **[`stack`](stack.md)**: Basic information about the product, including the title, rating, and a description.
- **[`subtitle`](subtitle.md)**: Text that provides additional information about its containing element.
- **[`text`](text.md)**: The text used to describe the surrounding elements.
- **[`title`](title.md)**: The title describing its containing element.

##### Example

The following listing shows the TVML for a `productBundleTemplate` example.

```xml
<document>
    <productBundleTemplate>
        <background>
        </background>
        <banner>
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
                <text>Follow the adventures of a determined developer</text>
                <description handlesOverflow ="true">The story of a development team that loves to cook and makes an app for ordering soup. Follow their journey across the country to WWDC, and the meals they make along the way.</description>
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
            <heroImg src="path to images on your server/Cooking_Show_720x1080.png" />
        </banner>
        <shelf>
            <header>
                <title>3 Episodes</title>
            </header>
            <section>
                <lockup>
                    <img src="path to images on your server/Cooking_Show_250x375_A.png" width="150" height="226" />
                    <title>Turn</title>
                </lockup>
                <lockup>
                    <img src="path to images on your server/Cooking_Show_250x375_B.png" width="150" height="226" />
                    <title>Road</title>
                </lockup>
                <lockup>
                    <img src="path to images on your server/Cooking_Show_250x375_C.png" width="150" height="226" />
                    <title>Helicopter</title>
                </lockup>
            </section>
        </shelf>
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
                    <text>Subtitles for the deaf and Hard of Hearing (SDH) refer to subtitles in the original language with the addition of relevant non-dialog information.</text>
                </info>
            </infoTable>
        </productInfo>
    </productBundleTemplate>
</document>
```

The following figures show the two pages created using the above example. The first figure shows what appears immediately onscreen, while the second figure shows what the user sees after navigating down the screen.

![Screenshot showing a sample product bundle. An image of the series is on the right and a description on the left. A row of episodes is at the bottom of the screen.](/images/com.apple.TVML/productbundletemplate-2@2x.png)

![Screenshot showing the second page of the product bundle. The top row contains reviews and ratings, the middle row contains actor informations, and the bottom row contains general information about the product bundle.](/images/com.apple.TVML/productbundletemplate-3@2x.png)

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
- [productTemplate](producttemplate.md)
  Displays detailed information about a single product.
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/productbundletemplate)*