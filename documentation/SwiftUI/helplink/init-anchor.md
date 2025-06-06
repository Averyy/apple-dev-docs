# init(anchor:)

**Framework**: SwiftUI  
**Kind**: init

Constructs a new help link with the specified anchor in the main app bundle’s book.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(anchor: NSHelpManager.AnchorName)
```

#### Discussion

The main app bundle book name is defined by the `CFBundleHelpBookName` key in its Info.plist file.

## Parameters

- `anchor`: The anchor within the help book to open to.

## See Also

- [init(action: () -> Void)](helplink/init(action:).md)
  Constructs a new help link with the specified action.
- [init(destination: URL)](helplink/init(destination:).md)
  Constructs a new help link that opens the specified destination URL.
- [init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)](helplink/init(anchor:book:).md)
  Constructs a new help link with the specified anchor and book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/helplink/init(anchor:))*