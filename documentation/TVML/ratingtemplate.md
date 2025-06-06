# ratingTemplate

**Framework**: TVML

Displays a rating for an item.

#### Overview

Use the `ratingTemplate` element to display a rating for an item. The following figure shows the basic layout for a `ratingTemplate` page. The theme for the rating template defaults to the system preference.

![Layout diagram showing a title area above a rating area.](https://docs-assets.developer.apple.com/published/5e0f80e80961edce4fb4115afe226fd7/ratingtemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `ratingTemplate` element in TVML format.

```xml
<document>
    <ratingTemplate>
        <title>…</title>
        <ratingBadge></ratingBadge>
    </ratingTemplate>
</document>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `ratingTemplate` example. The example displays a title and a set of rating badge images, such as stars. The filled rating badge images indicate the current rating for that title. The value attribute indicates that the example title has an 80 percent favorable rating, or 4 of 5 stars.

```xml
<document>
    <ratingTemplate>
        <title>WWDC Roadtrip</title>
        <ratingBadge value="0.8"></ratingBadge>
    </ratingTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a title and 4 of 5 rating stars filled in.](https://docs-assets.developer.apple.com/published/58081fddd58d0ffa662961ac2bcb4377/ratingtemplate-2%402x.png)

## Topics

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
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/ratingtemplate)*