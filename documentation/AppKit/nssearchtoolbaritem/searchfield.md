# searchField

**Framework**: AppKit  
**Kind**: property

The search field inside the toolbar item.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var searchField: NSSearchField { get set }
```

#### Discussion

When you set `searchField` to `nil`, it uses the default configuration for the toolbar item, and inherits the item’s properties and layout constraints. However, if you want to customize the search field, you’ll need to add those settings before assigning it to the toolbar item. For more information about customizing a search field, see [`NSSearchField`](nssearchfield.md).

## See Also

- [var preferredWidthForSearchField: CGFloat](nssearchtoolbaritem/preferredwidthforsearchfield.md)
  The preferred width for the toolbar item when it has keyboard focus.
- [var resignsFirstResponderWithCancel: Bool](nssearchtoolbaritem/resignsfirstresponderwithcancel.md)
  A Boolean value that enables the cancel button in the search field to resign the first responder in addition to clearing the contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchtoolbaritem/searchfield)*