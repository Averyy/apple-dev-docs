# document

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The document associated with the window controller.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var document: AnyObject? { get set }
```

```objc
@property (assign, nullable) id document;
```

#### Discussion

The value of this property is `nil` if no document is associated with the window. When a window controller is added to a document’s list of window controllers, the document uses this property to set the window controller’s document; you should not set this property. AppKit uses this property to access the document for relevant next-responder messages.

## See Also

### Accessing the Document
- [func setDocumentEdited(Bool)](./setdocumentedited%28_%29.md)
  Sets the document edited flag for the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/document)*