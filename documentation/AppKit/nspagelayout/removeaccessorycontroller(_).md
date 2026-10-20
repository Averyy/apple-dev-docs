# removeAccessoryController(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified controller of an accessory view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func removeAccessoryController(_ accessoryController: NSViewController)
```

```objc
- (void) removeAccessoryController:(NSViewController *) accessoryController;
```

## Parameters

- `accessoryController`: The controller to remove.

## See Also

### Customizing the page setup dialog
- [func addAccessoryController(NSViewController)](./addaccessorycontroller%28_%29.md)
  Adds the specified controller of an accessory view to be presented in the page setup panel.
- [var accessoryControllers: [NSViewController]](./accessorycontrollers.md)
  An array of accessory view controllers belonging to the page layout panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/removeaccessorycontroller(_:))*