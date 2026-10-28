# endSearchInteraction()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Ends a search interaction by giving up the first responder and adjusting the size of the search field to the available width for the toolbar item if necessary.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func endSearchInteraction()
```

```objc
- (void) endSearchInteraction;
```

## Discussion

Use [`beginSearchInteraction()`](./beginsearchinteraction%28%29.md) and [`endSearchInteraction()`](./endsearchinteraction%28%29.md) to programmatically control a search.

## See Also

### Controlling search interactions
- [func beginSearchInteraction()](./beginsearchinteraction%28%29.md)
  Starts a search interaction and moves the keyboard focus to the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchtoolbaritem/endsearchinteraction())*