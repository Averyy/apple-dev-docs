# monogramLockup

**Framework**: TVML

Creates a monogram using a person’s image or initials.

#### Overview

The `monogramLockup` element creates a white circle that contains the image or initials of the person identified in the title. Use the `src` element to place an image inside of the circle. If no image is added, initials are centered in the circle, based on the `firstName` and `lastName` attributes in the `monogram` element. Here’s an example of a monogramLockup displaying an actor’s infomation.

```xml
<monogramLockup>
    <monogram firstName="Anne" lastName="Johnson"/>
    <title>Anne Johnson</title>
    <subtitle>Actor</subtitle>
</monogramLockup>
```

##### Subelements of Monogramlockup

- [`monogram`](monogram.md)
- [`subtitle`](subtitle.md)
- [`title`](title.md)

##### Elements That Use Monogramlockup

- [`section`](section.md)

## Topics

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
- [buttonLockup](buttonlockup.md)
  Creates a button that can also have a badge associated with it.
- [listItemLockup](listitemlockup.md)
  Contains a new list item.
- [lockup](lockup.md)
  Contains several elements that are treated as a single element.
- [overlay](overlay.md)
  Displays elements on top of other elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/monogramlockup)*