# activityItemsConfiguration

**Framework**: AppKit  
**Kind**: property

The custom object from an app built with Mac Catalyst that provides the items to share.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)? { get set }
```

#### Discussion

Use this object to provide the set of items to share from your macOS window.

## See Also

- [var delegate: (any NSSharingServicePickerToolbarItemDelegate)?](nssharingservicepickertoolbaritem/delegate.md)
  The custom object from your app that provides the items to share.
- [protocol NSSharingServicePickerToolbarItemDelegate](nssharingservicepickertoolbaritemdelegate.md)
  An interface that provides the content to share from the macOS share sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertoolbaritem/activityitemsconfiguration)*