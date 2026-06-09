# visibilityPriority

**Framework**: UIKit  
**Kind**: property

Visibility priority for this item when placed in a button bar.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var visibilityPriority: UIBarButtonItemVisibilityPriority { get set }
```

#### Discussion

Items with higher priority values are preserved longer when space is constrained. When an item is placed in an implicit group, the group inherits this priority.

The default value is `UIBarButtonItemVisibilityPriorityStandard`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/visibilitypriority)*