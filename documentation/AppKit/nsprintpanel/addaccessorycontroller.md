# addAccessoryController(_:)

**Framework**: AppKit  
**Kind**: method

Adds a custom controller to the Print panel to manage an accessory view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func addAccessoryController(_ accessoryController: any NSViewController & NSPrintPanelAccessorizing)
```

#### Discussion

You can invoke this method multiple times to add multiple accessory views to the receiver’s Print panel.

The title for the accessory view is obtained from the `title` method of the view controller object.

## Parameters

- `accessoryController`: The view controller that manages your custom accessory views.

## See Also

- [func removeAccessoryController(any NSViewController & NSPrintPanelAccessorizing)](nsprintpanel/removeaccessorycontroller(_:).md)
  Removes the specified controller and accessory view from the Print panel.
- [protocol NSPrintPanelAccessorizing](nsprintpanelaccessorizing.md)
  A set of methods that a Print panel object can use to get information from a printing accessory controller.
- [var accessoryControllers: [NSViewController]](nsprintpanel/accessorycontrollers.md)
  The array of controller objects that manage the Print panel’s accessory views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/addaccessorycontroller(_:))*