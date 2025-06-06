# endSearchInteraction()

**Framework**: AppKit  
**Kind**: method

Ends a search interaction by giving up the first responder and adjusting the size of the search field to the available width for the toolbar item if necessary.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
func endSearchInteraction()
```

#### Discussion

Use [`beginSearchInteraction()`](nssearchtoolbaritem/beginsearchinteraction().md) and [`endSearchInteraction()`](nssearchtoolbaritem/endsearchinteraction().md) to programmatically control a search.

## See Also

- [func beginSearchInteraction()](nssearchtoolbaritem/beginsearchinteraction.md)
  Starts a search interaction and moves the keyboard focus to the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchtoolbaritem/endsearchinteraction())*