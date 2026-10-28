# init(anchor:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Constructs a new help link with the specified anchor in the main app bundle’s book.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency init(anchor: NSHelpManager.AnchorName)
```

## Discussion

The main app bundle book name is defined by the `CFBundleHelpBookName` key in its Info.plist file.

## Parameters

- `anchor`: The anchor within the help book to open to.

## See Also

### Creating a help link
- [init(action: () -> Void)](./init%28action%29.md)
  Constructs a new help link with the specified action.
- [init(destination: URL)](./init%28destination%29.md)
  Constructs a new help link that opens the specified destination URL.
- [init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)](./init%28anchor,book%29.md)
  Constructs a new help link with the specified anchor and book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/helplink/init(anchor:))*