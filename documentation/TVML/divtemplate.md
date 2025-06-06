# divTemplate

**Framework**: TVML

Provides the ability to create pages that don’t conform to a layout defined by another template.

#### Overview

There is no built-in layout for contained elements. The `divTemplate` element creates a view where the elements it contains are arranged using the `tv-align` and `tv-position` styles. Containing elements are centered by default. The following figure shows the positions inside of the `divTemplate` element. The `divTemplate` element should only be used when you can’t use another template to achieve the look you want. The theme for the div template defaults to the system preference.

![Layout diagram showing the positions other elements can be placed in.](https://docs-assets.developer.apple.com/published/8ab94a6903cb538652ca1484db33c75a/divtemplate-1%402x.png)

Elements contained in the same position are arranged from the top of the cell to the bottom, in the same order in which they are specified in the `divTemplate` element. You can specify a `<background><img /></background>` that displays a background image inside of the `divTemplate`. The background image is top-aligned and is fitted to the size of the `divTemplate` while keeping the image’s original aspect ratio. Text wrapping inside of the `divTemplate` only occurs in the `header`, `center`, and `footer` positions.

## Topics

### Valid TVML Styles
- [tv-align](tv-align.md)
  Aligns an element horizontally inside its parent.
- [tv-position](tv-position.md)
  Sets the position of an element inside of its parent element.
### Valid TVML Attributes
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
- [compilationTemplate](compilationtemplate.md)
  Displays information about a single media item and its components.
- [descriptiveAlertTemplate](descriptivealerttemplate.md)
  Displays large amounts of important information to the user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/divtemplate)*