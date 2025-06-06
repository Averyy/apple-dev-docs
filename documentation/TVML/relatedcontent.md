# relatedContent

**Framework**: TVML

Contains elements that are related to another element.

#### Overview

This element is often used to display the related content when another element is brought into focus. Here’s an example that contains a `lockup` inside of a `relatedContent` element.

```xml
<relatedContent>
    <lockup>
        <img src="path to image goes here" />
        <title>Title 1</title>
    </lockup>
</relatedContent
```

##### Subelements of Relatedcontent

- [`activityIndicator`](activityindicator.md)
- [`grid`](grid.md)
- [`heroImg`](heroimg.md)
- [`itemBanner`](itembanner.md)
- [`lockup`](lockup.md)

##### Elements That Use Relatedcontent

- [`list`](list.md)
- [`listItemLockup`](listitemlockup.md)

## Topics

### Valid TVML Styles
- [height](element-shaping-height.md)
  Specifies the height of an element.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [placeholder](placeholder.md)
  Contains elements that are not directly evaluated by the template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/relatedcontent)*