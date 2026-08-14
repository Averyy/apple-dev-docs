# documentBrowser(_:applicationActivitiesForDocumentURLs:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for additional activities when displaying an activity view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, applicationActivitiesForDocumentURLs documentURLs: [URL]) -> [UIActivity]
```

## Mentions

- [Adding custom actions and activities](adding-custom-actions-and-activities.md)

#### Return Value

An array of custom [`UIActivity`](uiactivity.md) objects.

#### Discussion

The document browser displays an activity view when the user shares a document (for example, when the user long presses a document and then chooses Share from the Edit Menu).

Implement this method to add custom activities to the activity view. Create and return an array containing your custom [`UIActivity`](uiactivity.md) subclasses. Your [`UIActivity`](uiactivity.md) subclasses should perform actions on the URLs passed to this method.

> **Note**:  Do not assume that the URL array contains only one URL. The user can place the document browser into Select mode and select multiple documents to share, even if the document browser’s [`allowsPickingMultipleItems`](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md) property is [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `controller`: The current document browser.
- `documentURLs`: The URL of one or more documents to share.

## See Also

- [func documentBrowser(UIDocumentBrowserViewController, willPresent: UIActivityViewController)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:willpresent:).md)
  Tells the delegate that the document browser will display an activity view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:applicationactivitiesfordocumenturls:))*