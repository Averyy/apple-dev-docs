# NSSharingServicePickerToolbarItemDelegate

**Framework**: AppKit  
**Kind**: protocol

An interface that provides the content to share from the macOS share sheet.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSSharingServicePickerToolbarItemDelegate : NSSharingServicePickerDelegate
```

#### Overview

Adopt the [`NSSharingServicePickerToolbarItemDelegate`](nssharingservicepickertoolbaritemdelegate.md) protocol in one of your app’s custom types and use it to provide shareable content. Assign your delegate object to an [`NSSharingServicePickerToolbarItem`](nssharingservicepickertoolbaritem.md) object you add to your window’s toolbar.

## Topics

### Providing the Items to Share
- [func items(for: NSSharingServicePickerToolbarItem) -> [Any]](nssharingservicepickertoolbaritemdelegate/items(for:).md)
  Asks the delegate for the items to share.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSharingServicePickerDelegate](nssharingservicepickerdelegate.md)

## See Also

- [var delegate: (any NSSharingServicePickerToolbarItemDelegate)?](nssharingservicepickertoolbaritem/delegate.md)
  The custom object from your app that provides the items to share.
- [var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)?](nssharingservicepickertoolbaritem/activityitemsconfiguration.md)
  The custom object from an app built with Mac Catalyst that provides the items to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertoolbaritemdelegate)*