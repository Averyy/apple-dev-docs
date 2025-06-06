# lockup

**Framework**: TVML

Contains several elements that are treated as a single element.

#### Overview

Here’s an example of a section that contains two `lockup` elements that represent movie posters.

```xml
<section>
    <lockup>
        <img src="path to images on your server/Car_Movie_453x255_C.png" width="453" height="255" />
        <title>Scene 1</title>
    </lockup>
    <lockup>
        <img src="path to images on your server/Car_Movie_500x600.png" width="500" height="600" />
        <title>Scene 2</title>
    </lockup>
</section>
```

##### Subelements of Lockup

- [`badge`](badge.md)
- [`description`](description.md)
- [`img`](img.md)
- [`organizer`](organizer.md)
- [`overlay`](overlay.md)
- [`title`](title.md)

##### Elements That Use Lockup

- [`relatedContent`](relatedcontent.md)
- [`section`](section.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [width](element-shaping-width.md)
  Specifies how wide an element is.
### Valid TVML Attributes
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [button](button.md)
  Displays a button icon the user can click to initiate an action.
- [buttonLockup](buttonlockup.md)
  Creates a button that can also have a badge associated with it.
- [listItemLockup](listitemlockup.md)
  Contains a new list item.
- [monogramLockup](monogramlockup.md)
  Creates a monogram using a person’s image or initials.
- [overlay](overlay.md)
  Displays elements on top of other elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/lockup)*