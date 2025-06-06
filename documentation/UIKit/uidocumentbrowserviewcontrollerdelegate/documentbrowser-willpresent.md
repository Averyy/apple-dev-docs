# documentBrowser(_:willPresent:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the document browser will display an activity view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, willPresent activityViewController: UIActivityViewController)
```

#### Discussion

The document browser displays an activity view when the user shares a document (for example, when the user long presses a document and then chooses Share from the Edit Menu).

Implement this method to customize the activity view before it is displayed. For example, you could exclude any system-provided activities that are inappropriate for your app (see the [`UIActivityViewController`](uiactivityviewcontroller.md) class’s [`excludedActivityTypes`](uiactivityviewcontroller/excludedactivitytypes.md) property).

## Parameters

- `controller`: The current document browser.
- `activityViewController`: The activity view controller to be displayed.

## See Also

- [func documentBrowser(UIDocumentBrowserViewController, applicationActivitiesForDocumentURLs: [URL]) -> [UIActivity]](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:applicationactivitiesfordocumenturls:).md)
  Asks the delegate for additional activities when displaying an activity view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:willpresent:))*