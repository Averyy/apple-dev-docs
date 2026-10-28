# allowsDuplicatesInToolbar

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar item can appear more than once in a toolbar.

**Availability**:
- macOS 10.0+ - Deprecated in 15.0

> **Deprecated**: Duplicates are no longer supported.

## Declaration

```swift
var allowsDuplicatesInToolbar: Bool { get }
```

```objc
@property (readonly) BOOL allowsDuplicatesInToolbar;
```

## Discussion

If the value in this property is [`true`](../../Swift/true.md), the toolbar allows someone to drag more than one copy of the toolbar item from the customization palette. If the value of this property is [`false`](../../Swift/false.md), the toolbar prevents someone from dragging more than one copy of the item from the customization palette.

By default, if an item with the same identifier is already in the toolbar, dragging it in again will effectively move it to the new position.

## See Also

### Deprecated
- [var minSize: NSSize](./minsize.md)
  The toolbar item’s minimum size.
- [var maxSize: NSSize](./maxsize.md)
  The toolbar item’s maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/allowsduplicatesintoolbar)*