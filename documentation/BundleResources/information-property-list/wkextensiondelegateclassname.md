# WKExtensionDelegateClassName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of your watchOS app’s extension delegate.

**Availability**:
- watchOS 2.0+

## Details

- **Name**: `WKExtensionDelegateClassName`
- **Type**: string

#### Discussion

This key provides the name of a class that adopts the [`WKExtensionDelegate`](../../WatchKit/wkextensiondelegate.md) protocol. Xcode automatically includes this key in the WatchKit extension’s information property list when you create a watchOS project from a template. You only modify this value when you rename or replace the extension delegate.

## See Also

### Extensions and services
- [NSExtension](./nsextension.md)
  The properties of an app extension.
- [NSServices](./nsservices.md)
  The services provided by an app.
- [UIApplicationShortcutWidget](./uiapplicationshortcutwidget.md)
  The bundle ID of the widget that’s available as a Home screen quick action in apps that have more than one widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wkextensiondelegateclassname)*