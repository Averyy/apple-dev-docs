# searchMenuTemplate

**Framework**: AppKit  
**Kind**: property

The menu object used to dynamically construct the search field’s pop-up icon menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var searchMenuTemplate: NSMenu? { get set }
```

#### Discussion

The cell looks for the tag constants described in [`Menu tags`](menu-tags.md) to determine how to populate the menu with items related to recent searches. For an example of how you might set up the search menu template, see [`Configuring a Search Menu`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/Articles/MenuTemplate.html#//apple_ref/doc/uid/20002245).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/searchmenutemplate)*