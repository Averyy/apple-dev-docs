# document

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The document that the controller presents or edits.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
var document: UIDocument? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIDocument * document;
```

#### Discussion

This property represents the document that the document view controller displays. The default value of this property is `nil`. When the value of the `document` property is `nil`, the document view controller presents an empty state view with a message to “Select a document by tapping the ‘Documents’ button at the top.”

When the value of this property is not `nil`, the document view controller displays the document.

## See Also

### Managing the document view
- [func openDocument(completionHandler: (Bool) -> Void)](./opendocument%28completionhandler%29.md)
  Opens a document in a document view controller from outside the document view controller.
- [func documentDidOpen()](./documentdidopen%28%29.md)
  Provides an opportunity to configure the view after the system loads the controller’s document into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/document)*