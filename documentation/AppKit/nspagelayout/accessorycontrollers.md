# accessoryControllers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of accessory view controllers belonging to the page layout panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var accessoryControllers: [NSViewController] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSViewController *> * accessoryControllers;
```

## Discussion

The `NSViewController` instances representing the accessory view controllers belonging to the receiver.

## See Also

### Customizing the page setup dialog
- [func addAccessoryController(NSViewController)](./addaccessorycontroller%28_%29.md)
  Adds the specified controller of an accessory view to be presented in the page setup panel.
- [func removeAccessoryController(NSViewController)](./removeaccessorycontroller%28_%29.md)
  Removes the specified controller of an accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/accessorycontrollers)*