# init(document:)

**Framework**: UIKit  
**Kind**: init

Creates a document view controller with a document.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(document: UIDocument?)
```

#### Return Value

A newly initialized [`UIDocumentViewController`](uidocumentviewcontroller.md) object.

#### Discussion

The document view controller opens and displays the document that you specify. If you don’t provide custom values, the new view controller gets its title and other information from the document itself.

## Parameters

- `document`: The document that the view controller presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/init(document:))*