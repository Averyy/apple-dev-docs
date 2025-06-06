# formTemplate

**Framework**: TVML

Provides the ability to gather information from the user.

#### Overview

Use the `formTemplate` element to gather information from the user; for example, requiring a password to access your app. The banner area can contain an image and a description of your product. The user enters text in the text field directly below the banner using the automatically generated keyboard. Use the footer area to contain any user interaction buttons. The following figure shows the basic layout for a `formTemplate` page. The theme for the form template defaults to the system preference.

![Layout diagram showing a banner area containing an image and description at the top, a text field followed by a keyboard below, and a footer area at the bottom.](https://docs-assets.developer.apple.com/published/d621d3a6bfc16a1c7eee6103b8d11b51/formtemplate-1%402x.png)

##### Form Template

The following listing shows the main elements of the `formTemplate` element in TVML format.

```xml
<formTemplate>
    <background>
        …
    </background>
    <banner>
        <img />
        <description>…</description>
    </banner>
    <textField>…</textField>
    <footer>…</footer>
</formTemplate>
```

###### Element Descriptions

##### Example

The following listing shows the TVML for a `formTemplate` example. The interactive keyboard is automatically created. The footer area contains a button that can submit the user input. Modify your main JavaScript file to accept the user input from the button. For more information on available JavaScript functions, see [`TVMLKit JS`](https://developer.apple.com/documentation/tvmljs).

```xml
<document>
    <formTemplate>
        <banner>
            <img src="path to images on your server/Car_Movie_800X400.png" width="800" height="400"/>
            <description>Enter email for access</description>
        </banner>
        <textField>tclark@example.com</textField>
        <footer>
            <button>
                <text>Submit</text>
            </button>
        </footer>
    </formTemplate>
</document>
```

The following figure shows the output for the above example:

![Screenshot showing a product image and a prompt for the user’s email address. A keyboard is displayed for email entry.](https://docs-assets.developer.apple.com/published/d3b7fe4b6132d785e0d64812b3bf45c3/formtemplate-2%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/formtemplate)*