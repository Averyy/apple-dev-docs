# beginSearchInteraction()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts a search interaction and moves the keyboard focus to the search field.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func beginSearchInteraction()
```

```objc
- (void) beginSearchInteraction;
```

#### Discussion

If the system displays a compressed search field, starting the search interaction expands the field to the width stored in the [`preferredWidthForSearchField`](./preferredwidthforsearchfield.md) property and moves the keyboard focus into the search field. Use [`beginSearchInteraction()`](./beginsearchinteraction%28%29.md) and [`endSearchInteraction()`](./endsearchinteraction%28%29.md) to programmatically control a search.

## See Also

### Controlling search interactions
- [func endSearchInteraction()](./endsearchinteraction%28%29.md)
  Ends a search interaction by giving up the first responder and adjusting the size of the search field to the available width for the toolbar item if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchtoolbaritem/beginsearchinteraction())*