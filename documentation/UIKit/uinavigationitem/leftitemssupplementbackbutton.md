# leftItemsSupplementBackButton

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the left items display in addition to the Back button.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var leftItemsSupplementBackButton: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL leftItemsSupplementBackButton;
```

#### Discussion

Normally, the presence of custom left bar button items causes the Back button to be removed in favor of the custom items. Setting this property to [`true`](../../Swift/true.md) causes the items in the [`leftBarButtonItems`](./leftbarbuttonitems.md) or [`leftBarButtonItem`](./leftbarbuttonitem.md) property to be displayed to the right of the Back button — that is, they’re displayed in addition to, not instead of, the Back button. When set to [`false`](../../Swift/false.md), the items in those properties are displayed instead of the Back button. The default value of this property is [`false`](../../Swift/false.md).

The value in the [`hidesBackButton`](./hidesbackbutton.md) property still determines whether the Back button is actually displayed.

## See Also

### Getting and setting properties
- [var prompt: String?](./prompt.md)
  A single line of text that displays at the top of the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/leftitemssupplementbackbutton)*