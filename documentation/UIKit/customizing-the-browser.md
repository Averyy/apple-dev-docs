# Customizing the browser

**Framework**: UIKit

Customize the document browser’s look and behavior.

#### Overview

You can set the browser’s appearance, create document thumbnails, and modify the browser’s behavior.

##### Set the Browsers Appearance

Change the browser’s appearance by setting the [`browserUserInterfaceStyle`](uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property.md) property. The document browser view controller supports white, light, and dark appearances.

##### Create Document Thumbnails or Icons

The system automatically provides thumbnails or icons for supported document types. If your app uses a custom or third-party document type, you can create a Thumbnail extension for that type. For more information, see [`QLThumbnailProvider`](https://developer.apple.com/documentation/QuickLookThumbnailing/QLThumbnailProvider).

If you don’t provide a Thumbnail extension, the system can create a document icon based on your app icon. To enable automatic icon creation, go to the Project navigator, choose the target, click Info, and then do the following:

1. Declare support for the document’s UTI in the Document Type section.
2. For any custom document types that you create, export the UTI in the Exported UTIs section.
3. For any third-party document types used by your app, import the UTI in the Imported UTIs section.

For more information, see [`Set the supported document types`](setting-up-a-document-browser-app#Set-the-supported-document-types.md).

Your app’s icon only appears in the Files app or document browser when the following are all true:

- The system doesn’t automatically provide a thumbnail for the UTI.
- The system doesn’t already provide an icon for the UTI.
- The user hasn’t installed a Thumbnail extension for the UTI.
- Your app both declares document type support for the UTI and declares the UTI as an exported or imported type.

##### Add Document Previews

The system automatically provides previews for supported document types. If your app uses a custom or third-party document type, you can create a Preview extension for that type.

For more information, see [`Quick Look`](https://developer.apple.com/documentation/Quartz/quick-look).

##### Modify the Browsers Behavior

You can control the following behaviors:

- The type of documents the browser opens
- Whether the browser opens multiple files at the same time
- Whether the browser creates new documents

###### Set Allowed Document Types

You set the list of allowed document types when you create the browser. Pass an array of uniform type identifier (UTI) strings to the [`UIDocumentBrowserViewController`](uidocumentbrowserviewcontroller.md) class’s [`init(forOpeningFilesWithContentTypes:)`](uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:).md) method. If you pass `nil`, the browser uses the document types specified by the [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) key in the app’s `Info.plist` file.

For detailed instructions on setting the [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) key, see [`Set the supported document types`](setting-up-a-document-browser-app#Set-the-supported-document-types.md)).

The following example programmatically creates a document browser for `.txt` files:

```swift
let browser = UIDocumentBrowserViewController(forOpeningFilesWithContentTypes: ["public.plain-text"])
```

###### Enable Multiple Document Selection

By default, users can select only one item at a time. To enable multiple document selection, set the document browser’s [`allowsPickingMultipleItems`](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

###### Enable New Document Creation

To let users create new documents, you must do the following:

- Set the browser’s [`allowsDocumentCreation`](uidocumentbrowserviewcontroller/allowsdocumentcreation.md) property to [`true`](https://developer.apple.com/documentation/Foundation/NSExpression/true) (the default value).
- Implement the [`UIDocumentBrowserViewControllerDelegate`](uidocumentbrowserviewcontrollerdelegate.md) object’s [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md) method.

After these steps are completed, the system automatically includes an Add button (+) in the document browser’s navigation bar.

When the user taps the Add button, the system calls the [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md) method. In your implementation, you can present a custom user interface, where users can configure the document. For example, you might show a list of document templates.

Create a new document and save it to a temporary location. As soon as the document is saved, call the provided `importHandler`. To confirm the request, pass in the document’s temporary URL and the import mode ([`UIDocumentBrowserViewController.ImportMode.copy`](uidocumentbrowserviewcontroller/importmode/copy.md) or [`UIDocumentBrowserViewController.ImportMode.move`](uidocumentbrowserviewcontroller/importmode/move.md)). To cancel the request, pass `nil` and [`UIDocumentBrowserViewController.ImportMode.none`](uidocumentbrowserviewcontroller/importmode/none.md).

> ❗ **Important**:  You must always call the `importHandler`. If you can’t create a new document, pass `nil` for the URL and [`UIDocumentBrowserViewController.ImportMode.none`](uidocumentbrowserviewcontroller/importmode/none.md) for the import mode.

## See Also

- [Adding custom actions and activities](adding-custom-actions-and-activities.md)
  Add custom document browser actions, activities, and bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/customizing-the-browser)*