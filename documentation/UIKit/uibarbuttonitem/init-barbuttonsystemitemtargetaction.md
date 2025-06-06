# init(barButtonSystemItem:target:action:)

**Framework**: UIKit  
**Kind**: init

Creates an item using the specified system item, target, and action.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(barButtonSystemItem systemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)
```

#### Return Value

A newly initialized [`UIBarButtonItem`](uibarbuttonitem.md).

## Parameters

- `systemItem`: The system item to use as the first item on the bar. For possible values, see  .
- `target`: The object that receives the   message.
- `action`: The action to send to   when a person selects this item.

## See Also

- [convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(image:style:target:action:).md)
  Creates an item using the specified image, style, target, and action.
- [convenience init(title: String?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(title:style:target:action:).md)
  Creates an item using the specified title, style, target, and action.
- [convenience init(systemItem: UIBarButtonItem.SystemItem, primaryAction: UIAction?, menu: UIMenu?)](uibarbuttonitem/init(systemitem:primaryaction:menu:).md)
  Creates an item using the specified system item, primary action, and context menu.
- [UIBarButtonItem.SystemItem](uibarbuttonitem/systemitem.md)
  Constants that define system-supplied images for bar button items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(barbuttonsystemitem:target:action:))*