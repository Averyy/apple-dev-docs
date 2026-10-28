# WKHostingController

**Framework**: SwiftUI  
**Kind**: class  
**Role**: Class

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency class WKHostingController<Body> where Body : View
```

## Overview

A [`WKHostingController`](./wkhostingcontroller.md) presents and manages your app’s main interface using SwiftUI views. You must subclass [`WKHostingController`](./wkhostingcontroller.md) and override the [`body`](./wkhostingcontroller/body.md) property to provide the set of SwiftUI views you want to display. Display the content of your hosting controller as you would any other [`WKInterfaceController`](../WatchKit/wkinterfacecontroller.md) object. For example, you can include it as one of your app’s root interface controllers, or present it modally.

## Topics

### Creating a hosting controller object
- [init()](./wkhostingcontroller/init%28%29.md)
  Creates a hosting controller object that you can use to implement your app’s main interface using SwiftUI views
### Getting the root view
- [var body: Body](./wkhostingcontroller/body.md)
  The root view of the view hierarchy to display for your interface controller.
### Updating the root view
- [func updateBodyIfNeeded()](./wkhostingcontroller/updatebodyifneeded%28%29.md)
  Updates the interface controller’s set of views immediately, if updates are pending.
- [func setNeedsBodyUpdate()](./wkhostingcontroller/setneedsbodyupdate%28%29.md)
  Invalidates the current SwiftUI views and triggers an update during the next cycle.

## Relationships

### Inherits From
- [WKInterfaceController](../WatchKit/wkinterfacecontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Displaying SwiftUI views in WatchKit
- [class WKUserNotificationHostingController](./wkusernotificationhostingcontroller.md)
  A WatchKit user notification interface controller that hosts a SwiftUI view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkhostingcontroller)*