# leftItemsSupplementBackButton

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the left items display in addition to the Back button.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var leftItemsSupplementBackButton: Bool { get set }
```

#### Discussion

Normally, the presence of custom left bar button items causes the Back button to be removed in favor of the custom items. Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) causes the items in the [`leftBarButtonItems`](uinavigationitem/leftbarbuttonitems.md) or [`leftBarButtonItem`](uinavigationitem/leftbarbuttonitem.md) property to be displayed to the right of the Back button — that is, they’re displayed in addition to, not instead of, the Back button. When set to [`false`](https://developer.apple.com/documentation/swift/false), the items in those properties are displayed instead of the Back button. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

The value in the [`hidesBackButton`](uinavigationitem/hidesbackbutton.md) property still determines whether the Back button is actually displayed.

## See Also

- [var prompt: String?](uinavigationitem/prompt.md)
  A single line of text that displays at the top of the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/leftitemssupplementbackbutton)*