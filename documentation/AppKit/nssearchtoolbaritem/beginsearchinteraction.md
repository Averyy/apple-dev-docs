# beginSearchInteraction()

**Framework**: AppKit  
**Kind**: method

Starts a search interaction and moves the keyboard focus to the search field.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
func beginSearchInteraction()
```

#### Discussion

If the system displays a compressed search field, starting the search interaction expands the field to the width stored in the [`preferredWidthForSearchField`](nssearchtoolbaritem/preferredwidthforsearchfield.md) property and moves the keyboard focus into the search field. Use [`beginSearchInteraction()`](nssearchtoolbaritem/beginsearchinteraction().md) and [`endSearchInteraction()`](nssearchtoolbaritem/endsearchinteraction().md) to programmatically control a search.

## See Also

- [func endSearchInteraction()](nssearchtoolbaritem/endsearchinteraction.md)
  Ends a search interaction by giving up the first responder and adjusting the size of the search field to the available width for the toolbar item if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchtoolbaritem/beginsearchinteraction())*