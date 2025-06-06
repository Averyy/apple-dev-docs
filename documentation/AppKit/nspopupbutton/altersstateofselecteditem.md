# altersStateOfSelectedItem

**Framework**: AppKit  
**Kind**: property

When the value of this property is `YES`, the selected menu item’s `state` is set to `NSControlStateValueOn`. When the value of this property is `NO`, the menu item’s `state` is not changed. When this property changes, the `state` of the currently selected item is updated appropriately. This property is ignored for pull-down buttons.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
var altersStateOfSelectedItem: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/altersstateofselecteditem)*