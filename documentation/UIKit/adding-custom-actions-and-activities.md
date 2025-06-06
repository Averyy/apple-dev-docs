# Adding custom actions and activities

**Framework**: UIKit

Add custom document browser actions, activities, and bar items.

#### Overview

There are three different ways to add custom actions to the document browser:

- Add document browser actions to the navigation bar or Edit Menu.
- Add activities to the activity view.
- Add bar items to the navigation bar.

##### Add Document Browser Actions

By default, the system provides a number of standard actions (copy, move, rename, delete, and share). To add custom actions, assign an array of [`UIDocumentBrowserAction`](uidocumentbrowseraction.md) objects to the browser’s [`customActions`](uidocumentbrowserviewcontroller/customactions.md) property.

Document browser actions can be accessed in two ways:

-  actions appear in the navigation bar when the user places the browser into the Select mode.
-  actions appear when the user long presses on a document or folder.

When triggered, these actions are passed the URLs of the currently selected items.

##### Add Activities

The browser displays an activity view when the user taps the Share button (for example, when the user long presses on a document or folder and selects Share from the Edit Menu).

To add custom activities to the activity view, implement your [`UIDocumentBrowserViewControllerDelegate`](uidocumentbrowserviewcontrollerdelegate.md) object’s [`documentBrowser(_:applicationActivitiesForDocumentURLs:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:applicationactivitiesfordocumenturls:).md) method and return an array of custom [`UIActivity`](uiactivity.md) objects.

Your delegate object is passed an array of URLs for the currently selected items. You can store and use these URLs in your [`UIActivity`](uiactivity.md) subclass.

For more information, see [`Sharing and Actions`](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/extensions/sharing-and-actions/).

##### Add Bar Button Items

Use the [`additionalLeadingNavigationBarButtonItems`](uidocumentbrowserviewcontroller/additionalleadingnavigationbarbuttonitems.md) and [`additionalTrailingNavigationBarButtonItems`](uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems.md) methods to add buttons to the navigation bar.

Actions triggered by these buttons don’t have access to the browser’s content or to the URLs of selected items. Use bar button items for global actions only (actions that don’t affect a specific document or folder).

## See Also

- [Customizing the browser](customizing-the-browser.md)
  Customize the document browser’s look and behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adding-custom-actions-and-activities)*