# visibilityPriority

**Framework**: AppKit  
**Kind**: property

Determines which items are shown in a bar when space is limited.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var visibilityPriority: NSTouchBarItem.Priority { get set }
```

#### Discussion

The bar hides items of lower priority when there is not enough space to show all items. Use this property to specify the relative priority of the items in your bar.

## See Also

- [NSTouchBarItem.Priority](nstouchbaritem/priority.md)
  Priorities for the visibility of a Touch Bar item.
- [var isVisible: Bool](nstouchbaritem/isvisible.md)
  A Boolean value that reflects whether or not the item is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/visibilitypriority)*