# callAsFunction(_:)

**Framework**: SwiftUI  
**Kind**: method

Presents a new document window for the in-memory document returned by the provided closure.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> sending D) where D : ReadableDocument
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`newDocument`](environmentvalues/newdocument.md) action with a [`ReadableDocument`](readabledocument.md) factory.

The factory closure runs when SwiftUI needs the document instance. SwiftUI then injects the instance into the matching [`DocumentGroup`](documentgroup.md) and presents its window. The matching document group is the first creatable group whose readable content types overlap with `D.readableContentTypes`.

## Parameters

- `newDocument`: A closure that produces the in-memory document to present.

## See Also

- [func callAsFunction(contentType: UTType)](newdocumentaction/callasfunction(contenttype:).md)
  Presents a new document window.
- [func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) -> Void)](newdocumentaction/callasfunction(contenttype:preparedocument:).md)
  Presents a new document window with preset contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(_:))*