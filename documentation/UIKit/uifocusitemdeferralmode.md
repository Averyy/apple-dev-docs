# UIFocusItemDeferralMode

**Framework**: UIKit  
**Kind**: enum

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum UIFocusItemDeferralMode
```

## Topics

### Enumeration Cases
- [UIFocusItemDeferralMode.always](uifocusitemdeferralmode/always.md)
  Always defer focus for this item, even if deferral is disabled right now. This means a programmatic update to this item would result in focus disappearing until the user interacts with the focus engine again.
- [UIFocusItemDeferralMode.automatic](uifocusitemdeferralmode/automatic.md)
  Use the system default behavior.
- [UIFocusItemDeferralMode.never](uifocusitemdeferralmode/never.md)
  Never defer focus for this item. When a programmatic focus update lands on this item, it will always be and appear focused even if focus deferral is currently enabled.
### Initializers
- [init?(rawValue: Int)](uifocusitemdeferralmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIAccessibility.ExpandedStatus](uiaccessibility/expandedstatus.md)
- [UITextFormattingViewController.ComponentSize](uitextformattingviewcontroller/componentsize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitemdeferralmode)*