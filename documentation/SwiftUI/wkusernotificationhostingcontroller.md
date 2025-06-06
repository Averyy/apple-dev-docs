# WKUserNotificationHostingController

**Framework**: SwiftUI  
**Kind**: class

A WatchKit user notification interface controller that hosts a SwiftUI view hierarchy.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency class WKUserNotificationHostingController<Body> where Body : View
```

#### Overview

A [`WKUserNotificationHostingController`](wkusernotificationhostingcontroller.md) presents and manages your app’s notification interface using SwiftUI views. You must subclass [`WKUserNotificationHostingController`](wkusernotificationhostingcontroller.md) and override the [`body`](wkusernotificationhostingcontroller/body.md) property to provide the set of SwiftUI views you want to display. In the storyboard of your watch app, specify the name of your custom class for your dynamic interactive interface.

## Topics

### Creating a hosting controller object
- [init()](wkusernotificationhostingcontroller/init.md)
  Creates a notification hosting controller object that you can use to implement your notification interfaces using SwiftUI views.
### Getting the root view
- [var body: Body](wkusernotificationhostingcontroller/body.md)
  The root view of the view hierarchy to display for your notification interface.
### Configuring the notification
- [class var coalescedDescriptionFormat: String?](wkusernotificationhostingcontroller/coalesceddescriptionformat.md)
  The format string to display when multiple notifications of the same type arrive simultaneously. If you specify a custom string, you can use the %d variable to reflect the number of notifications. If `nil` format will be the system default.
- [class var isInteractive: Bool](wkusernotificationhostingcontroller/isinteractive.md)
  If the notification should accept user input.
- [class var sashColor: Color?](wkusernotificationhostingcontroller/sashcolor.md)
  Color to use within the sash of the long look interface. If `nil` the sash will be the default system color.
- [class var subtitleColor: Color?](wkusernotificationhostingcontroller/subtitlecolor.md)
  The color to apply to the subtitle text displayed in the short look interface. If `nil` the text will be the default system color.
- [class var titleColor: Color?](wkusernotificationhostingcontroller/titlecolor.md)
  The color to apply to the text displayed in the sash. If `nil` the text will be the default system color.
- [class var wantsSashBlur: Bool](wkusernotificationhostingcontroller/wantssashblur.md)
  If the sash should include a blur over the background.

## Relationships

### Inherits From
- [WKUserNotificationInterfaceController](../WatchKit/WKUserNotificationInterfaceController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKHostingController](wkhostingcontroller.md)
  A WatchKit interface controller that hosts a SwiftUI view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller)*