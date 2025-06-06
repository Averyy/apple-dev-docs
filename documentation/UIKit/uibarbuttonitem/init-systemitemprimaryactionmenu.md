# init(systemItem:primaryAction:menu:)

**Framework**: UIKit  
**Kind**: init

Creates an item using the specified system item, primary action, and context menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(systemItem: UIBarButtonItem.SystemItem, primaryAction: UIAction? = nil, menu: UIMenu? = nil)
```

#### Return Value

A newly initialized [`UIBarButtonItem`](uibarbuttonitem.md).

## Parameters

- `systemItem`: The system item to use as the first item on the bar. For possible values, see  .
- `primaryAction`: A   to associate with the item. The system item doesn’t use the action to configure its title and image.
- `menu`: The menu to present. The context menu displays in response to a person tapping the item.

## See Also

- [convenience init(barButtonSystemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)](uibarbuttonitem/init(barbuttonsystemitem:target:action:).md)
  Creates an item using the specified system item, target, and action.
- [UIBarButtonItem.SystemItem](uibarbuttonitem/systemitem.md)
  Constants that define system-supplied images for bar button items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(systemitem:primaryaction:menu:))*