# loadingTemplate

**Framework**: Tvml

Displays a spinner and description on the screen.

#### Overview

Use the `loadingTemplate` element to display a spinner and description of why the spinner is being displayed; for example, an interim page showing that the requested page is being loaded. A spinner is automatically presented when the page is displayed, and you can add text to tell your users what is happening. The following figure shows the basic layout for a `layoutTemplate` page. The theme for the loading template defaults to the system preference.

> **Note**: When a user performs an action to bring up a new page and the new page is not immediately ready, a `loadingTemplate` page should be presented. After the new page is ready, replace the `loadingTemplate` with the new page onto the navigation stack.

![Layout diagram showing a title area and a spinner.](https://docs-assets.developer.apple.com/published/b97d2cd006e891cee13c5d8721a7bc46/loadingtemplate-1%402x.png)

##### Main Elements

The following listing shows main elements of the `loadingTemplate` in TVML format.

```xml
<document>
   <loadingTemplate>
      <activityIndicator>
         <title>Title</title>
      </activityIndicator>
   </loadingTemplate>
</document>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a loadingTemplate example.

```xml
<document>
   <loadingTemplate>
      <activityIndicator>
         <title>Loading requested page</title>
      </activityIndicator>
   </loadingTemplate>
</document>
```

The following figure shows the output of the above example:

![Screenshot of a loading page with a spinner icon.](https://docs-assets.developer.apple.com/published/17e70b9a9eace22aa56e09194bd71695/loadingtemplate-2%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/TVML/loadingtemplate)*