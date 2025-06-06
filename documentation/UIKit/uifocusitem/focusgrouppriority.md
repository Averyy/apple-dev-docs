# focusGroupPriority

**Framework**: UIKit  
**Kind**: property

The importance of the item within a focus group, used by the focus system to determine the group’s primary item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var focusGroupPriority: UIFocusGroupPriority { get }
```

#### Discussion

The system automatically assigns each focusable item in a focus group one of the predefined system priorities. The system assigns the [`currentlyFocused`](uifocusgrouppriority/currentlyfocused.md) priority to the focused item, [`previouslyFocused`](uifocusgrouppriority/previouslyfocused.md) to the group’s previous focused item, and [`ignored`](uifocusgrouppriority/ignored.md) for all other items. The visible item with the highest priority is the group’s primary item.

You can override the default priority of an item to customize the primary item of a group. When setting a custom priority, you can only increase the item’s priority above its system-provided value, not decrease it. The system-provided priority is always the minimum priority applied for the item. The system ignores any priority lower than `0`.

## See Also

- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem/focusgrouppriority)*