# alertTemplate

**Framework**: TVML

Displays important information to the user.

#### Overview

Use the `alertTemplate` element to display important information, such as a message telling the user to perform an action before continuing. At a minimum, provide a description of the alert and a button so the user can take any required actions. The following figure shows the basic layout for an `alertTemplate` page. The theme for the alert template defaults to the system preference.

![Layout diagram showing title and description areas at the top, and a button area followed by a text area below.](https://docs-assets.developer.apple.com/published/0d680fb326cadffca7e6694e5bb86beb/alerttemplate-1%402x.png)

##### Main Elements

The following listing shows the main elements of the `alertTemplate` element in TVML format:

```xml
<alertTemplate>
   <background>
      …
   </background>
   <title>…</title>
   <description>…</description>
   <button>
      <text>…</text>
   </button>
   <text>…</text>
</alertTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for an `alertTemplate` example:

```xml
<document>
   <alertTemplate>
      <title>Update Available</title>
      <description>Get the latest tvOS version</description>
      <button>
         <text>Update Now</text>
      </button>
      <button>
         <text>Cancel</text>
      </button>
   </alertTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot prompting the user to update the Apple TV. Two buttons below the prompt allow the user to accept or cancel the update.](https://docs-assets.developer.apple.com/published/6290f7ee1979bec25272f5e113c8d556/alerttemplate-2%402x.png)

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
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/alerttemplate)*