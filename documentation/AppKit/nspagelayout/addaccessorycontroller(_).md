# addAccessoryController(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified controller of an accessory view to be presented in the page setup panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func addAccessoryController(_ accessoryController: NSViewController)
```

```objc
- (void) addAccessoryController:(NSViewController *) accessoryController;
```

## Parameters

- `accessoryController`: The controller to add.

## See Also

### Customizing the page setup dialog
- [func removeAccessoryController(NSViewController)](./removeaccessorycontroller%28_%29.md)
  Removes the specified controller of an accessory view.
- [var accessoryControllers: [NSViewController]](./accessorycontrollers.md)
  An array of accessory view controllers belonging to the page layout panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/addaccessorycontroller(_:))*