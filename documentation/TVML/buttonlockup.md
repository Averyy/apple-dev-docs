# buttonLockup

**Framework**: TVML

Creates a button that can also have a badge associated with it.

#### Overview

Images on buttons are often used to indicate the function of the button. Use the `buttonLockup` element to add a badge to the the button. Here’s an example that shows a button with the preview icon and a title.

```xml
<buttonLockup>
    <badge src="resource://button-preview" />
    <title>Preview</title>
</buttonLockup>
```

##### Subelements of Buttonlockup

- [`badge`](badge.md)
- [`title`](title.md)

##### Elements That Use Buttonlockup

- [`organizer`](organizer.md)
- [`row`](row.md)

## Topics

### Valid TVML Styles
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
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

- [button](button.md)
  Displays a button icon the user can click to initiate an action.
- [listItemLockup](listitemlockup.md)
  Contains a new list item.
- [lockup](lockup.md)
  Contains several elements that are treated as a single element.
- [monogramLockup](monogramlockup.md)
  Creates a monogram using a person’s image or initials.
- [overlay](overlay.md)
  Displays elements on top of other elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/buttonlockup)*