# isEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the menu item is enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

This property has no effect unless the menu in which the item will be added or is already a part of has been sent `setAutoenablesItems:NO`. If a menu item is disabled, its keyboard equivalent is also disabled. See the `NSMenuValidation` informal protocol specification for cautions regarding this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/isenabled)*