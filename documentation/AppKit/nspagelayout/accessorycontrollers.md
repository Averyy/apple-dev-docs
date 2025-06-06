# accessoryControllers

**Framework**: AppKit  
**Kind**: property

An array of accessory view controllers belonging to the page layout panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var accessoryControllers: [NSViewController] { get }
```

#### Discussion

The `NSViewController` instances representing the accessory view controllers belonging to the receiver.

## See Also

- [func addAccessoryController(NSViewController)](nspagelayout/addaccessorycontroller(_:).md)
  Adds the specified controller of an accessory view to be presented in the page setup panel.
- [func removeAccessoryController(NSViewController)](nspagelayout/removeaccessorycontroller(_:).md)
  Removes the specified controller of an accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/accessorycontrollers)*