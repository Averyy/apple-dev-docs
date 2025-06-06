# init(destination:)

**Framework**: SwiftUI  
**Kind**: init

Constructs a new help link that opens the specified destination URL.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(destination: URL)
```

#### Discussion

Use this initializer when you want the standard help button appearance that opens a link to a website.

You can override the default behavior when the button is clicked by setting the [`openURL`](environmentvalues/openurl.md) environment value with a custom [`OpenURLAction`](openurlaction.md).

## Parameters

- `destination`: The URL to open when the button is clicked.

## See Also

- [init(action: () -> Void)](helplink/init(action:).md)
  Constructs a new help link with the specified action.
- [init(anchor: NSHelpManager.AnchorName)](helplink/init(anchor:).md)
  Constructs a new help link with the specified anchor in the main app bundle’s book.
- [init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)](helplink/init(anchor:book:).md)
  Constructs a new help link with the specified anchor and book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/helplink/init(destination:))*