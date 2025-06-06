# itemBanner

**Framework**: TVML

Displays information associated with an element.

#### Overview

Use `itemBanner` element to display information inside of a `relatedContent` element. Here’s an example that displays an image and three buttons related to a media item.

```xml
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
```

##### Subelements of Itembanner

- [`heroImg`](heroimg.md)
- [`img`](img.md)
- [`row`](row.md)

##### Elements That Use Itembanner

- [`relatedContent`](relatedcontent.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [width](element-shaping-width.md)
  Specifies how wide an element is.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [banner](banner.md)
  Displays information along the top of a TVML page.
- [identityBanner](identitybanner.md)
  Displays information about an artist or performer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/itembanner)*