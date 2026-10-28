# NCWidgetProviding

**Framework**: Notification Center  
**Kind**: protocol  
**Role**: Protocol

The interface for customizing the appearance and behavior of a Today widget.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 10.0+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
protocol NCWidgetProviding : NSObjectProtocol
```

*macOS*

```swift
protocol NCWidgetProviding : NSExtensionRequestHandling
```

*iOS, iPadOS, Mac Catalyst*

```objc
@protocol NCWidgetProviding <NSObject>
```

*macOS*

```objc
@protocol NCWidgetProviding <NSExtensionRequestHandling>
```

## Overview

The `NCWidgetProviding` protocol allows customization of the appearance and behavior of a Today widget.

## Topics

### Customizing the Display
- [func widgetMarginInsets(forProposedMarginInsets: UIEdgeInsets) -> UIEdgeInsets](./ncwidgetproviding/widgetmargininsets%28forproposedmargininsets%29.md)
  Called to let a widget accept the default margin inset values or return custom values to use instead.
- [func widgetActiveDisplayModeDidChange(NCWidgetDisplayMode, withMaximumSize: CGSize)](./ncwidgetproviding/widgetactivedisplaymodedidchange%28_,withmaximumsize%29.md)
  Called when the active display mode changes.
- [enum NCWidgetDisplayMode](./ncwidgetdisplaymode.md)
  The modes that can be toggled between when the user activates the More button for a widget running in iOS.
### Updating a Widget’s Contents
- [func widgetPerformUpdate(completionHandler: (NCUpdateResult) -> Void)](./ncwidgetproviding/widgetperformupdate%28completionhandler%29.md)
  Called to give a widget an opportunity to update its contents.
- [enum NCUpdateResult](./ncupdateresult.md)
  The result of updating a widget’s state.
### Supporting Editing
- [var widgetAllowsEditing: Bool](./ncwidgetproviding/widgetallowsediting.md)
  A Boolean value indicating whether the widget can be edited by users.
- [func widgetDidBeginEditing()](./ncwidgetproviding/widgetdidbeginediting%28%29.md)
  Called when a user chooses the widget’s begin editing button.
- [func widgetDidEndEditing()](./ncwidgetproviding/widgetdidendediting%28%29.md)
  Called when a widget’s editing session ends.

## Relationships

### Inherits From
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Core Widget
- [class NCWidgetController](./ncwidgetcontroller.md)
  An object used to specify whether a Today widget has content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding)*