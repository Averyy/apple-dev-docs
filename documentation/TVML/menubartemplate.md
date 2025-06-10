# menuBarTemplate

**Framework**: TVML

Creates a page with items along the top and related information below.

#### Overview

Use the `menuBarTemplate` to display a list of selectable items across the top of the screen. Users can move between menu bar items to change the information displayed below the menu bar. The following figure shows the basic layout for a `menuBarTemplate` page. The theme for the menu bar template defaults to the system preference.

![Layout diagram showing a menu bar area at the top and a related content area below.](https://docs-assets.developer.apple.com/published/177505cf6a027229a8287dbf3d699d01/menubartemplate-1%402x.png)

> **Note**: You can display up to seven items in the menu bar.

##### Main Elements

The following listing shows the main elements of the `menuBarTemplate` element in TVML format.

```xml
<document>
    <menuBarTemplate>
        <menuBar>
            <menuItem>
                <title>…</title>
            </menuItem>
        </menuBar>
    </menuBarTemplate>
</document>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `menuBarTemplate` example. The example shows the menu bar along the top of the screen. Expand the controlling JavaScript file in order to show content for each item in the menu bar. For more information, see [`TVMLKit JS`](https://developer.apple.com/documentation/tvmljs).

```xml
<document>
    <menuBarTemplate>
        <menuBar>
            <menuItem id="navigation_top_movies" data-identifier="list">
                <title>Top Movies</title>
            </menuItem>
            <menuItem id="navigation_genres" data-identifier="index">
                <title>Genres</title>
            </menuItem>
            <menuItem id="navigation_search" data-identifier="search">
                <title>Search</title>
            </menuItem>
            <menuItem id="navigation_edit" data-identifier="edit">
                <title>Edit</title>
            </menuItem>
            <menuItem id="navigation_settings_add" data-identifier="add_settings">
                <title>Add Settings</title>
            </menuItem>
        </menuBar>
    </menuBarTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a menu bar with user options along the top of the screen.](https://docs-assets.developer.apple.com/published/7f5a8f53e2127507aeb4a0799c71b725/menubartemplate-2%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/menubartemplate)*