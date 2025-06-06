# compilationTemplate

**Framework**: TVML

Displays information about a single media item and its components.

#### Overview

Use the `compilationTemplate` element to display information about one product that is made up of several distinct pieces; for example, an album and all of the songs that it contains. The header area on the left side of the screen contains general product information. Directly underneath the header area are several section areas that group like types of information; for example, one section can contain all of the songs on the album. The related content on the right side of the screen contains any images associated with the product and buttons that the user can use to interact with the product, such as Play and Buy buttons. The following figure shows the basic layout for a `compilationTemplate` page. The theme for the compilation template defaults to the system preference.

![Layout diagram showing header and section areas on the left side and related content on the right.](https://docs-assets.developer.apple.com/published/c5690aa8089a1839847213800543d7eb/compilationtemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `compilationTemplate` element in TVML format:

```xml
<compilationTemplate>
    <background>
        …
    </background>
    <list>
        <relatedContent>
            <itemBanner>
                …
            </itemBanner>
        </relatedContent>
        <header>
            …
        </header>
        <section>
            <header>
                <title>Title</title>
            </header>
            <listItemLockup>
                …
            </listItemLockup>
        </section>
    </list>
</compilationTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `compilationTemplate` example. The example displays a list on the left side that contains information about the album and a list of available songs. The right side of the display contains an image of the album and buttons prompting the user to buy, rate, or shuffle the music.

```xml
<document>
    <compilationTemplate theme="light">
        <list>
            <relatedContent>
                <itemBanner>
                    <heroImg src="path to images on your server/Car_Movie_720x1080" />
                    <row>
                        <buttonLockup>
                            <badge src="resource://button-add"/>
                            <title>Add</title>
                        </buttonLockup>
                        <buttonLockup>
                            <badge src="resource://button-rate"/>
                            <title>Rate</title>
                        </buttonLockup>
                        <buttonLockup>
                            <badge src="resource://button-shuffle"/>
                            <title>Shuffle</title>
                        </buttonLockup>
                    </row>
                </itemBanner>
            </relatedContent>
            <header>
                <title>WWDC Roadtrip Soundtrack</title>
                <subtitle>Various Artists</subtitle>
                <row>
                    <text>Instrumental</text>
                    <text>5 Songs</text>
                    <text>2015</text>
                </row>
            </header>
            <section>
                <description>Songs from your favorite movie</description>
            </section>
            <section>
                <listItemLockup>
                    <ordinal minLength="2">1</ordinal>
                    <title>Opening sequence</title>
                    <decorationLabel>11:14</decorationLabel>
                </listItemLockup>
                <listItemLockup>
                    <ordinal minLength="2">2</ordinal>
                    <title>Fight song</title>
                    <decorationLabel>3:47</decorationLabel>
                </listItemLockup>
                <listItemLockup>
                    <ordinal minLength="2">3</ordinal>
                    <title>Love theme</title>
                    <decorationLabel>6:48</decorationLabel>
                </listItemLockup>
                <listItemLockup>
                    <ordinal minLength="2">4</ordinal>
                    <title>Car chase</title>
                    <decorationLabel>5:21</decorationLabel>
                </listItemLockup>
                <listItemLockup>
                    <ordinal minLength="2">5</ordinal>
                    <title>End credit theme</title>
                    <decorationLabel>8:03</decorationLabel>
                </listItemLockup>
            </section>
        </list>
    </compilationTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a sample album listing. Title and song list are on the left side and cover art and buttons are on the right.](https://docs-assets.developer.apple.com/published/48d9da8a0d17eee6ed41534b91400b88/compilationtemplate-2%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/compilationtemplate)*