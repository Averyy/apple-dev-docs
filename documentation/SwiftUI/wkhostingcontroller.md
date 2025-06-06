# WKHostingController

**Framework**: SwiftUI  
**Kind**: class

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency class WKHostingController<Body> where Body : View
```

#### Overview

A [`WKHostingController`](wkhostingcontroller.md) presents and manages your app’s main interface using SwiftUI views. You must subclass [`WKHostingController`](wkhostingcontroller.md) and override the [`body`](wkhostingcontroller/body.md) property to provide the set of SwiftUI views you want to display. Display the content of your hosting controller as you would any other [`WKInterfaceController`](https://developer.apple.com/documentation/WatchKit/WKInterfaceController) object. For example, you can include it as one of your app’s root interface controllers, or present it modally.

## Topics

### Creating a hosting controller object
- [init()](wkhostingcontroller/init.md)
  Creates a hosting controller object that you can use to implement your app’s main interface using SwiftUI views
### Getting the root view
- [var body: Body](wkhostingcontroller/body.md)
  The root view of the view hierarchy to display for your interface controller.
### Updating the root view
- [func updateBodyIfNeeded()](wkhostingcontroller/updatebodyifneeded.md)
  Updates the interface controller’s set of views immediately, if updates are pending.
- [func setNeedsBodyUpdate()](wkhostingcontroller/setneedsbodyupdate.md)
  Invalidates the current SwiftUI views and triggers an update during the next cycle.

## Relationships

### Inherits From
- [WKInterfaceController](../WatchKit/WKInterfaceController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKUserNotificationHostingController](wkusernotificationhostingcontroller.md)
  A WatchKit user notification interface controller that hosts a SwiftUI view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkhostingcontroller)*