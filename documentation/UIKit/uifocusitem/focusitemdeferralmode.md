# focusItemDeferralMode

**Framework**: UIKit  
**Kind**: property

If this property is present and returns `UIFocusItemDeferralModeNever`, the focus deferral will not be enabled again after the user engagement timeout has expired if this item is currently focused and programmatic focus updates pointing to this item will be executed immediatly. If it returns `UIFocusItemDeferralModeAlways` focus will always be deferred when this item is supposed to be focused. Does nothing when focus deferral is not supported on the platform.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional var focusItemDeferralMode: UIFocusItemDeferralMode { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem/focusitemdeferralmode)*