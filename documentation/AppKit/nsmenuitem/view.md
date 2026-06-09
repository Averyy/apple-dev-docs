# view

**Framework**: AppKit  
**Kind**: property

The content view for the menu item.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var view: NSView? { get set }
```

#### Discussion

A menu item with a view does not draw its title, state, font, or other standard drawing attributes, and assigns drawing responsibility entirely to the view. Keyboard equivalents and type-select continue to use the key equivalent and title as normal. For more information, see [`NSMenuItem`](nsmenuitem.md).

By default, a menu item has a `nil` view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/view)*