# allowsDuplicatesInToolbar

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar item can appear more than once in a toolbar.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var allowsDuplicatesInToolbar: Bool { get }
```

#### Discussion

If the value in this property is [`true`](https://developer.apple.com/documentation/Swift/true), the toolbar allows someone to drag more than one copy of the toolbar item from the customization palette. If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the toolbar prevents someone from dragging more than one copy of the item from the customization palette.

By default, if an item with the same identifier is already in the toolbar, dragging it in again will effectively move it to the new position.

## See Also

- [var minSize: NSSize](nstoolbaritem/minsize.md)
  The toolbar item’s minimum size.
- [var maxSize: NSSize](nstoolbaritem/maxsize.md)
  The toolbar item’s maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/allowsduplicatesintoolbar)*