# NCWidgetProviding

**Framework**: Notification Center  
**Kind**: protocol

The interface for customizing the appearance and behavior of a Today widget.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.10+

## Declaration

```swift
protocol NCWidgetProviding : NSExtensionRequestHandling
```

#### Overview

The `NCWidgetProviding` protocol allows customization of the appearance and behavior of a Today widget.

## Topics

### Customizing the Display
- [func widgetMarginInsets(forProposedMarginInsets: UIEdgeInsets) -> UIEdgeInsets](ncwidgetproviding/widgetmargininsets(forproposedmargininsets:).md)
  Called to let a widget accept the default margin inset values or return custom values to use instead.
- [func widgetActiveDisplayModeDidChange(NCWidgetDisplayMode, withMaximumSize: CGSize)](ncwidgetproviding/widgetactivedisplaymodedidchange(_:withmaximumsize:).md)
  Called when the active display mode changes.
- [enum NCWidgetDisplayMode](ncwidgetdisplaymode.md)
  The modes that can be toggled between when the user activates the More button for a widget running in iOS.
### Updating a Widget’s Contents
- [func widgetPerformUpdate(completionHandler: (NCUpdateResult) -> Void)](ncwidgetproviding/widgetperformupdate(completionhandler:).md)
  Called to give a widget an opportunity to update its contents.
- [enum NCUpdateResult](ncupdateresult.md)
  The result of updating a widget’s state.
### Supporting Editing
- [var widgetAllowsEditing: Bool](ncwidgetproviding/widgetallowsediting.md)
  A Boolean value indicating whether the widget can be edited by users.
- [func widgetDidBeginEditing()](ncwidgetproviding/widgetdidbeginediting.md)
  Called when a user chooses the widget’s begin editing button.
- [func widgetDidEndEditing()](ncwidgetproviding/widgetdidendediting.md)
  Called when a widget’s editing session ends.

## Relationships

### Inherits From
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NCWidgetController](ncwidgetcontroller.md)
  An object used to specify whether a Today widget has content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding)*