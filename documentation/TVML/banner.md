# banner

**Framework**: TVML

Displays information along the top of a TVML page.

#### Overview

The type of information displayed depends on the type of template used. Here’s an example that places a banner with an image and some text inside of a `formTemplate` element.

```xml
<formTemplate>
   <banner>
      <img src="path to images on your server/Car_Movie_800X400.png" width="800" height="400"/>
      <description>Enter email for access</description>
   </banner>
   ...
</formTemplate>
```

##### Subelements of Banner

- [`background`](background.md)
- [`button`](button.md)
- [`description`](description.md)
- [`heroImg`](heroimg.md)
- [`img`](img.md)
- [`infoList`](infolist.md)
- [`row`](row.md)
- [`stack`](stack.md)
- [`title`](title.md)

##### Elements That Use Banner

- [`catalogTemplate`](catalogtemplate.md)
- [`compilationTemplate`](compilationtemplate.md)
- [`formTemplate`](formtemplate.md)
- [`listTemplate`](listtemplate.md)
- [`productBundleTemplate`](productbundletemplate.md)
- [`productTemplate`](producttemplate.md)
- [`showcaseTemplate`](showcasetemplate.md)
- [`stackTemplate`](stacktemplate.md)

## Topics

### Valid TVML Styles
- [height](element-shaping-height.md)
  Specifies the height of an element.
- [margin](margin.md)
  Specifies the spacing around an element.
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [tv-position](tv-position.md)
  Sets the position of an element inside of its parent element.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [identityBanner](identitybanner.md)
  Displays information about an artist or performer.
- [itemBanner](itembanner.md)
  Displays information associated with an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/banner)*