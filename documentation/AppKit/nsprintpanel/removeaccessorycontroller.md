# removeAccessoryController(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified controller and accessory view from the Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func removeAccessoryController(_ accessoryController: any NSViewController & NSPrintPanelAccessorizing)
```

#### Discussion

You use this method to remove any view controllers responsible for displaying accessory views you do not want to include in the Print panel.

## Parameters

- `accessoryController`: The view controller to remove.

## See Also

- [func addAccessoryController(any NSViewController & NSPrintPanelAccessorizing)](nsprintpanel/addaccessorycontroller(_:).md)
  Adds a custom controller to the Print panel to manage an accessory view.
- [protocol NSPrintPanelAccessorizing](nsprintpanelaccessorizing.md)
  A set of methods that a Print panel object can use to get information from a printing accessory controller.
- [var accessoryControllers: [NSViewController]](nsprintpanel/accessorycontrollers.md)
  The array of controller objects that manage the Print panel’s accessory views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/removeaccessorycontroller(_:))*