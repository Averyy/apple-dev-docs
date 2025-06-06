# descriptiveAlertTemplate

**Framework**: TVML

Displays large amounts of important information to the user.

#### Overview

Use the `descriptiveAlertTemplate` element to display a significant amount of important information, such as a Terms of Service page. A title is displayed at the top of the screen with a large text area directly below it. An area containing buttons is located along the bottom of the screen. The following figure shows the basic layout for a `descriptiveAlertTemplate` page. The theme for the descriptive alert template defaults to the system preference.

![Layout diagram showing title area at the top, a description area directly below it, and a row of buttons at the bottom.](https://docs-assets.developer.apple.com/published/84926fdf93e4192446093291c53d4ee4/descriptivealerttemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `descriptiveAlertTemplate` in TVML format.

```xml
<descriptiveAlertTemplate>
   <background>
      …
   </background>
   <title>Title</title>
   <img />
   <description>Description</description>
   <row>
      <button>
         …
      </button>
   </row>
</descriptiveAlertTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `descriptiveAlertTemplate` example.

```xml
<document>
   <descriptiveAlertTemplate>
      <title>Terms of Service</title>
      <description>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</description>
      <row>
         <button>
            <text>Accept</text>
         </button>
         <button>
            <text>Decline</text>
         </button>
      </row>
   </descriptiveAlertTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a Terms of Service example page. Two buttons let the user accept or decline the Terms of Service.](https://docs-assets.developer.apple.com/published/79daac79622f9956232bdb042555db97/descriptivealerttemplate-2%402x.png)

## Topics

### Valid TVML Attributes
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
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
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/descriptivealerttemplate)*