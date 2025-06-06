# init(anchor:book:)

**Framework**: SwiftUI  
**Kind**: init

Constructs a new help link with the specified anchor and book.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)
```

## Parameters

- `anchor`: The anchor within the help book to open to.
- `book`: The specific book name to open.

## See Also

- [init(action: () -> Void)](helplink/init(action:).md)
  Constructs a new help link with the specified action.
- [init(destination: URL)](helplink/init(destination:).md)
  Constructs a new help link that opens the specified destination URL.
- [init(anchor: NSHelpManager.AnchorName)](helplink/init(anchor:).md)
  Constructs a new help link with the specified anchor in the main app bundle’s book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/helplink/init(anchor:book:))*