# createDocumentAction(withIntent:)

**Framework**: UIKit  
**Kind**: method

Creates an action that uses the specified intent.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class func createDocumentAction(withIntent intent: UIDocument.CreationIntent) -> UIAction
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Discussion

Use this method to create an action that you can assign to your [`primaryAction`](uidocumentviewcontroller/launchoptions-swift.class/primaryaction.md) or [`secondaryAction`](uidocumentviewcontroller/launchoptions-swift.class/secondaryaction.md). When the system triggers the action, it calls your [`UIDocumentBrowserViewControllerDelegate`](uidocumentbrowserviewcontrollerdelegate.md) object’s [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md) method. For more information, see [`Customizing a document-based app’s launch experience`](customizing-a-document-based-app-s-launch-experience.md).

## Parameters

- `intent`: An intent that defines how your app creates the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/createdocumentaction(withintent:))*