# openDocument(completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Opens a document in a document view controller from outside the document view controller.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
func openDocument(completionHandler: @escaping (Bool) -> Void)
```

```swift
func openDocument() async -> Bool
```

```objc
- (void) openDocumentWithCompletionHandler:(void (^)(BOOL success)) completionHandler;
```

## Parameters

- `completionHandler`: The function that executes after the document view controller opens the document

## See Also

### Managing the document view
- [var document: UIDocument?](./document.md)
  The document that the controller presents or edits.
- [func documentDidOpen()](./documentdidopen%28%29.md)
  Provides an opportunity to configure the view after the system loads the controller’s document into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/opendocument(completionhandler:))*