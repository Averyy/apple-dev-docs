# NCWidgetController

**Framework**: Notification Center  
**Kind**: class

An object used to specify whether a Today widget has content to display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+

## Declaration

```swift
class NCWidgetController
```

#### Overview

The `NCWidgetController` class defines an object that both a Today widget and the containing app that delivers the widget can use to specify whether the widget has content to display. Because this class helps a widget and its containing app coordinate the display of the widget’s content, a widget that doesn’t communicate with its containing app is unlikely to use this class.

Typically, a widget appears in the Today view when it has content to display. If a currently running widget no longer has content to display, it can get a widget controller and set the flag in the [`setHasContent(_:forWidgetWithBundleIdentifier:)`](ncwidgetcontroller/sethascontent(_:forwidgetwithbundleidentifier:).md) method to `false`. If the containing app later determines that there is content this widget should display, the app can get a widget controller and update the flag, even while the widget isn’t running.

The `NCWidgetController` class should not be subclassed.

## Topics

### Getting a Widget Controller
- [class func widgetController() -> Self](ncwidgetcontroller/widgetcontroller.md)
  Returns a widget controller used to specify whether a widget has content to display.
### Specifying the Presence of Content
- [func setHasContent(Bool, forWidgetWithBundleIdentifier: String)](ncwidgetcontroller/sethascontent(_:forwidgetwithbundleidentifier:).md)
  Sets whether the specified widget has content to display.
### Type Methods
- [class func `default`() -> NCWidgetController](ncwidgetcontroller/default.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NCWidgetProviding](ncwidgetproviding.md)
  The interface for customizing the appearance and behavior of a Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller)*