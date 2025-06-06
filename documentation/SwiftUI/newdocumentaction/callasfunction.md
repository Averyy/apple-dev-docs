# callAsFunction(_:)

**Framework**: SwiftUI  
**Kind**: method

Presents a new document window.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping () -> D) where D : FileDocument
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`newDocument`](environmentvalues/newdocument.md) action:

```swift
newDocument(TextDocument(text: selectedText))
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `newDocument`: The new file document to present.

## See Also

- [func callAsFunction(contentType: UTType)](newdocumentaction/callasfunction(contenttype:).md)
  Presents a new document window.
- [func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) -> Void)](newdocumentaction/callasfunction(contenttype:preparedocument:).md)
  Presents a new document window with preset contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(_:))*