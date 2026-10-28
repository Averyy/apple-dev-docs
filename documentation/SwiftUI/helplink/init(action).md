# init(action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Constructs a new help link with the specified action.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency init(action: @escaping () -> Void)
```

## Discussion

Use this initializer when you want the standard help button appearance with a custom button action that does not open an article in an Apple Help book.

## Parameters

- `action`: The action to perform when the user clicks the button.

## See Also

### Creating a help link
- [init(destination: URL)](./init%28destination%29.md)
  Constructs a new help link that opens the specified destination URL.
- [init(anchor: NSHelpManager.AnchorName)](./init%28anchor%29.md)
  Constructs a new help link with the specified anchor in the main app bundle’s book.
- [init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)](./init%28anchor,book%29.md)
  Constructs a new help link with the specified anchor and book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/helplink/init(action:))*