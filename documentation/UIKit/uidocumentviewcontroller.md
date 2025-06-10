# UIDocumentViewController

**Framework**: UIKit  
**Kind**: class

A view controller that manages and presents a document stored locally or in the cloud.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDocumentViewController
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Overview

`UIDocumentViewController` presents a view that displays a [`document`](uidocumentviewcontroller/document.md). It manages opening, saving, and closing the document. You can use `UIDocumentViewController` to present documents from a [`UIDocumentBrowserViewController`](uidocumentbrowserviewcontroller.md), for instance. When you aren’t presenting documents from a `UIDocumentBrowserViewController`,  `UIDocumentViewController` displays a button that, when tapped, presents a picker a person can use to choose the document to display.

The document view controller’s [`document`](uidocumentviewcontroller/document.md) property is an optional [`UIDocument`](uidocument.md). While the `document` property value is `nil`, the document view controller displays a view depicting an empty state with the message, “No Document”. The empty state provides a prompt that reads “Select a document by tapping the ‘Documents’ button at the top.”

When the `document` property value is not `nil`, the document view controller displays the document. You configure the [`view`](uiviewcontroller/view.md) to display the document in the [`documentDidOpen()`](uidocumentviewcontroller/documentdidopen().md) callback method.

The navigation item automatically assigns its title menu, its [`UIDocumentProperties`](uidocumentproperties.md) object, undo and redo buttons, and [`renameDelegate`](uinavigationitem/renamedelegate-o32h.md) from information in the document view controller’s `document`.

`UIDocumentViewController` also provides sharing and drag and drop support, and key-commands for common actions such as undo and redo.

##### Subclassing Notes

`UIDocumentViewController` is an abstract base class that is meant to be subclassed. To create a subclass, you override two methods.

1. The system calls [`documentDidOpen()`](uidocumentviewcontroller/documentdidopen().md) when someone opens the document associated with the document view controller, or when an object assigns a previously opened document to the document view controller.
2. The system calls [`navigationItemDidUpdate()`](uidocumentviewcontroller/navigationitemdidupdate().md) every time `UIDocumentViewController` makes changes to its navigation item.

###### Open and Close Documents

When the document view controller opens the document associated with it, or when an object assigns an already opened document to the document view controller, the system calls [`documentDidOpen()`](uidocumentviewcontroller/documentdidopen().md). You can populate the view controller’s views to display the content of the document in this method:

```swift
override func documentDidOpen() {
    configureViewForCurrentDocument()
}
```

It’s good practice to configure the view in its own method and call that method in both `documentDidOpen()` and [`viewDidLoad()`](uiviewcontroller/viewdidload().md). There is no guarantee of the timing between when the system calls `documentDidOpen()` and when the system loads the view controller’s view, so check that the view loaded and the document opened before configuring your views.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    configureViewForCurrentDocument()
}

func configureViewForCurrentDocument() {
    guard let document = markdownDocument,
        !document.documentState.contains(.closed)
            && isViewLoaded else { return }
    // Configure views for document
}
```

###### Customize Navigation Items

While `UIDocumentViewController` automatically sets the document title and other navigation items using information from the document, you can customize these items by overriding the [`navigationItemDidUpdate()`](uidocumentviewcontroller/navigationitemdidupdate().md) method. The system calls `navigationItemDidUpdate()` every time `UIDocumentViewController` makes changes to the navigation item.

```swift
override func navigationItemDidUpdate() {
    // Customize the navigation item.
}
```

###### Add Sharing Drag and Drop and Undo and Redo

`UIDocumentViewController` automatically includes drag and drop, undo and redo, and sharing support. If you want undo and redo buttons to appear in your `UIDocumentViewController`, add a [`undoRedoItemGroup`](uidocumentviewcontroller/undoredoitemgroup.md) to the navigation bar and ensure that your custom `UIDocument` implements an undo manager. `UIDocumentViewController` sets the `hidden` property of this group, depending on the availability of an undo manager. It automatically enables or disables the buttons inside the group, as necessary.

###### Open a Document From Outside the Class

`UIDocumentViewController` automatically opens and closes its document. However, if you need to access a document from outside the document view controller, you can create a new instance of `UIDocumentViewController` and call its [`openDocument(completionHandler:)`](uidocumentviewcontroller/opendocument(completionhandler:).md) method.

In this sample code, a [`UIDocumentBrowserViewController`](uidocumentbrowserviewcontroller.md) presents a document using a `UIDocumentViewController`.

```swift
// Open a document.

class BrowserViewController: UIDocumentBrowserViewController {

    func presentDocument(_ document: MarkdownDocument) {
        let documentController = UIDocumentViewController(document: document)
        documentController.openDocument { success in
            if success {
                self.present(documentController, animated: true)
            }
        }
    }

}
```

`UIDocumentViewController` makes all the necessary callbacks, such as calling [`documentDidOpen()`](uidocumentviewcontroller/documentdidopen().md) and, when the document is open, it calls the completion handler you provided.

###### Use the Class As a Root View Controller

`To use a UIDocumentViewController` as the root view controller in an app, you need to declare the key “UIDocumentClass” for the relevant file type in your app’s info.plist. Set the document class to the `UIDocument` subclass you are using in your app.

If there is no browser view controller in the hierarchy, `UIDocumentViewController` displays a document button that opens a document picker in the navigation bar.

## Topics

### Creating a document view controller
- [init(document: UIDocument?)](uidocumentviewcontroller/init(document:).md)
  Creates a document view controller with a document.
### Managing the document view
- [var document: UIDocument?](uidocumentviewcontroller/document.md)
  The document that the controller presents or edits.
- [func openDocument(completionHandler: (Bool) -> Void)](uidocumentviewcontroller/opendocument(completionhandler:).md)
  Opens a document in a document view controller from outside the document view controller.
- [func documentDidOpen()](uidocumentviewcontroller/documentdidopen.md)
  Provides an opportunity to configure the view after the system loads the controller’s document into memory.
### Customizing navigation items
- [func navigationItemDidUpdate()](uidocumentviewcontroller/navigationitemdidupdate.md)
  Provides an opportunity to customize the navigation items after the navigation bar updates.
### Adding undo and redo functionality
- [var undoRedoItemGroup: UIBarButtonItemGroup](uidocumentviewcontroller/undoredoitemgroup.md)
  The group that contains the undo/redo buttons that this view controller adds to the navigation bar.
### Customizing the launch experience
- [var launchOptions: UIDocumentViewController.LaunchOptions](uidocumentviewcontroller/launchoptions-swift.property.md)
  Options that customize a document-based app’s launch view.
- [UIDocumentViewController.LaunchOptions](uidocumentviewcontroller/launchoptions-swift.class.md)
  Options for customizing the document launch view.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller)*