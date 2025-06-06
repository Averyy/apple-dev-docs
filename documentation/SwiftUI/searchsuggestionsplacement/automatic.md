# automatic

**Framework**: SwiftUI  
**Kind**: property

Search suggestions render automatically based on the surrounding context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var automatic: SearchSuggestionsPlacement { get }
```

#### Discussion

The behavior varies by platform:

- In iOS and iPadOS, suggestions render as a list overlaying the main content of the app.
- In macOS, suggestions render in a menu.
- In tvOS, suggestions render as a row underneath the search field.
- In watchOS, suggestions render in a list pushed onto the containing navigation stack.

## See Also

- [static var content: SearchSuggestionsPlacement](searchsuggestionsplacement/content.md)
  Search suggestions render in the main content of the app.
- [static var menu: SearchSuggestionsPlacement](searchsuggestionsplacement/menu.md)
  Search suggestions render inside of a menu attached to the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchsuggestionsplacement/automatic)*