# accessoryControllers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of controller objects that manage the Print panel’s accessory views.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var accessoryControllers: [NSViewController] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSViewController *> * accessoryControllers;
```

#### Discussion

This property contains an array of [`NSViewController`](../nsviewcontroller.md) objects, each of which represents an accessory view added using the [`addAccessoryController(_:)`](./addaccessorycontroller%28_%29.md) method.

## See Also

### Managing Accessory Views
- [func addAccessoryController(any NSViewController & NSPrintPanelAccessorizing)](./addaccessorycontroller%28_%29.md)
  Adds a custom controller to the Print panel to manage an accessory view.
- [func removeAccessoryController(any NSViewController & NSPrintPanelAccessorizing)](./removeaccessorycontroller%28_%29.md)
  Removes the specified controller and accessory view from the Print panel.
- [protocol NSPrintPanelAccessorizing](../nsprintpanelaccessorizing.md)
  A set of methods that a Print panel object can use to get information from a printing accessory controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/accessorycontrollers)*