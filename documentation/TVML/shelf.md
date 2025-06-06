# shelf

**Framework**: TVML

Displays elements horizontally and adds the ability to scroll to offscreen elements.

#### Overview

The `shelf` element is a horizontal row consisting of one or more elements. The user navigates along the items on a shelf by clicking left or right on the remote, and chooses an element by clicking the Select button on the remote. The generic shelf element structure is displayed first, followed by several standard shelf configurations. Here’s an example showing the basic layout of a `shelf` element.

```xml
<shelf>
    <header>
        <title>Viewers Also Watched</title>
    </header>
    <section>
        <lockup onselect="…"> //add link to other prodcut on your server here
            <imageStack>
                <img src="…" /> //add link to preview image for other product
            </imageStack>
            <title>Also Watched One</title>
        </lockup>
    </section>
</shelf>
```

There are several standard shelf configurations that are used to display related content.

##### Also Watched Shelf

The `shelf` element can display information about other products that have been watched by people who have also watched the selected product. The shelf displays the image you associate with the also-watched product, and the title is only displayed when the also-watched product is in focus. Here’s an example of a `shelf` element that contains three other products.

```xml
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
```

##### Cast and Crew Shelf

The `shelf` element can display information about the cast and crew associated with the product. Each person is represented by a large circle that contains the individual’s initials. Below the circle is the individual’s name and the name of the character they play. Here’s an example of a `shelf` element that contains three cast members.

```xml
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
```

##### Extras Shelf

The `shelf` element can display information about additional items included with the product. Common additional items include deleted scenes, extended scenes, and trailers. The listing below shows an example of a `shelf` element that contains a link to the online extras, a brief description of the extras, and a product trailer.

The extras shelf typically contains two sections. The first section contains an image of the additional items and a description of the items. Users can click the image to access the additional items. The second section contains a preview image of a trailer for the original product that users can click to view the trailer. Additional trailers require additional sections.

```xml
<shelf>
    <section>
        <header>
            <title>Product Extras</title>
        </header>
        <descriptionLockup>
            <img src="…"/> //add link to preview image for extras
            <text>Extras</text>
            <description>Enter text describing the item here</description>
            <text>Add text that talks about anything special included with this item or special requirements needed</text>
        </descriptionLockup
    </section>
    <section>
        <header>
            <title>Trailers</title>
        </header>
        <lockup onselect="…"> //add link to trailer on your server here
            <imageStack>
                <img src="…" /> //add link to preview image for trailer
            </imageStack>
            <title>Theatrical Trailer 2m</title>
        </lockup>
    </section>
</shelf>
```

##### Review and Ratings Shelf

The `shelf` element can display a list of ratings and reviews of the item it is associated with. Typically, a `lockup` element is displayed, followed by one or more `buttonLockup` elements. Common rating lockups contain information from iTunes or Rotten Tomatoes.

```xml
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
```

##### Subelements of Shelf

- [`header`](header.md)
- [`section`](section.md)
- [`text`](text.md)

##### Elements That Use Shelf

- [`alertTemplate`](alerttemplate.md)
- [`descriptiveAlertTemplate`](descriptivealerttemplate.md)
- [`footer`](footer.md)
- [`productBundleTemplate`](productbundletemplate.md)
- [`productTemplate`](producttemplate.md)
- [`separator`](separator.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [tv-interitem-spacing](tv-interitem-spacing.md)
  Specifies the spacing between child elements.
### Valid TVML Attributes
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
- [binding](binding.md)
  Associates information in a data item with an element.
- [centered](centered.md)
  Centers media items in a shelf.
- [itemID](itemid.md)
  Mark elements for reuse during DOM updates.
- [needsMoreThreshold](needsmorethreshold.md)
  Sets the amount of remaining screen lengths before firing the needs more event.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [rowCount](rowcount.md)
  Specifies the number of rows in a shelf.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [carousel](carousel.md)
  Arranges images in a row.
- [grid](grid.md)
  Arranges elements in a grid pattern.
- [imgDeck](imgdeck.md)
  Contains several images to be displayed at a later time.
- [infoTable](infotable.md)
  Displays contained element information in a vertical format, with each successive element directly below the previous element.
- [organizer](organizer.md)
  Creates a generic element with its contained elements arranged through TVML styles.
- [row](row.md)
  Displays elements horizontally.
- [section](section.md)
  Combines elements and acts as a single element.
- [stack](stack.md)
  Groups and lays out elements vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/shelf)*