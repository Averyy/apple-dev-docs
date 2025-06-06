# documentDidOpen()

**Framework**: UIKit  
**Kind**: method

Provides an opportunity to configure the view after the system loads the controller’s document into memory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func documentDidOpen()
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Discussion

The system calls this method after the document view controller opens its document, or when an object assigns an already opened document to the document view controller’s `document` property. Override this method to customize the views that present your document in the view:

```swift
override func documentDidOpen() {
    configureViewForCurrentDocument()
}
```

Configure the view in its own method and call that method in both `documentDidOpen()` and [`viewDidLoad()`](uiviewcontroller/viewdidload().md). There is no timing guarantee between when the system calls `documentDidOpen` and when it loads the view controller’s view.

## See Also

- [var document: UIDocument?](uidocumentviewcontroller/document.md)
  The document that the controller presents or edits.
- [func openDocument(completionHandler: (Bool) -> Void)](uidocumentviewcontroller/opendocument(completionhandler:).md)
  Opens a document in a document view controller from outside the document view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/documentdidopen())*