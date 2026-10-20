# currentlyFocused

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The focus group priority of the currently focused item, the highest possible priority.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
static var currentlyFocused: UIFocusGroupPriority { get }
```

```c
static const UIFocusGroupPriority UIFocusGroupPriorityCurrentlyFocused;
```

## See Also

### Constants
- [static var ignored: UIFocusGroupPriority](./ignored.md)
  The lowest focus group priority, assigned by default.
- [static var previouslyFocused: UIFocusGroupPriority](./previouslyfocused.md)
  The focus group priority of a previously focused item.
- [static var prioritized: UIFocusGroupPriority](./prioritized.md)
  The focus group priority that indicates an item is more important than others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusgrouppriority/currentlyfocused)*