# init(action:)

**Framework**: SwiftUI  
**Kind**: init

Constructs a new help link with the specified action.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(action: @escaping () -> Void)
```

#### Discussion

Use this initializer when you want the standard help button appearance with a custom button action that does not open an article in an Apple Help book.

## Parameters

- `action`: The action to perform when the user clicks the button.

## See Also

- [init(destination: URL)](helplink/init(destination:).md)
  Constructs a new help link that opens the specified destination URL.
- [init(anchor: NSHelpManager.AnchorName)](helplink/init(anchor:).md)
  Constructs a new help link with the specified anchor in the main app bundle’s book.
- [init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)](helplink/init(anchor:book:).md)
  Constructs a new help link with the specified anchor and book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/helplink/init(action:))*