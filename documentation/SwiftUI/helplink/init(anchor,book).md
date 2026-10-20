# init(anchor:book:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Constructs a new help link with the specified anchor and book.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)
```

## Parameters

- `anchor`: The anchor within the help book to open to.
- `book`: The specific book name to open.

## See Also

### Creating a help link
- [init(action: () -> Void)](./init%28action%29.md)
  Constructs a new help link with the specified action.
- [init(destination: URL)](./init%28destination%29.md)
  Constructs a new help link that opens the specified destination URL.
- [init(anchor: NSHelpManager.AnchorName)](./init%28anchor%29.md)
  Constructs a new help link with the specified anchor in the main app bundle’s book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/helplink/init(anchor:book:))*