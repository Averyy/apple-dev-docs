# delegate

**Framework**: AppKit  
**Kind**: property

The custom object from your app that provides the items to share.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
weak var delegate: (any NSSharingServicePickerToolbarItemDelegate)? { get set }
```

#### Discussion

Use your delegate object to provide the set of items you want to share from your window. If this property is `nil`, AppKit disables the toolbar item.

## See Also

- [protocol NSSharingServicePickerToolbarItemDelegate](nssharingservicepickertoolbaritemdelegate.md)
  An interface that provides the content to share from the macOS share sheet.
- [var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)?](nssharingservicepickertoolbaritem/activityitemsconfiguration.md)
  The custom object from an app built with Mac Catalyst that provides the items to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertoolbaritem/delegate)*