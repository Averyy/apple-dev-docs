# CPDashboardController

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A controller that provides shortcut buttons for the CarPlay Dashboard.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
class CPDashboardController
```

```objc
@interface CPDashboardController : NSObject
```

## Overview

A dashboard controller manages up to two shortcut buttons that CarPlay displays in the dashboard when there’s no active navigation session. You don’t create the dashboard controller. Instead, CarPlay creates one for you and passes it to the delegate of [`CPTemplateApplicationDashboardScene`](./cptemplateapplicationdashboardscene.md) when it connects the dashboard scene.

After receiving the controller, set [`shortcutButtons`](./cpdashboardcontroller/shortcutbuttons.md) to an array that contains a maximum of two shortcut buttons. CarPlay manages hiding or showing the buttons on the dashboard at the appropriate times.

## Topics

### Providing Dashboard Buttons
- [var shortcutButtons: [CPDashboardButton]](./cpdashboardcontroller/shortcutbuttons.md)
  An array of shortcut buttons to display on the CarPlay Dashboard.
- [class CPDashboardButton](./cpdashboardbutton.md)
  A shortcut button for placement on the CarPlay Dashboard.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing the Dashboard Controller
- [var dashboardController: CPDashboardController](./cptemplateapplicationdashboardscene/dashboardcontroller.md)
  The controller that manages the dashboard scene’s shortcut buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardcontroller)*