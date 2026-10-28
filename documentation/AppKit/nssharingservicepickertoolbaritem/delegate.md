# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The custom object from your app that provides the items to share.

**Availability**:
- macOS 10.15+

## Declaration

```swift
weak var delegate: (any NSSharingServicePickerToolbarItemDelegate)? { get set }
```

```objc
@property (weak) id<NSSharingServicePickerToolbarItemDelegate> delegate;
```

## Discussion

Use your delegate object to provide the set of items you want to share from your window. If this property is `nil`, AppKit disables the toolbar item.

## See Also

### Getting the Toolbar Items
- [protocol NSSharingServicePickerToolbarItemDelegate](../nssharingservicepickertoolbaritemdelegate.md)
  An interface that provides the content to share from the macOS share sheet.
- [var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)?](./activityitemsconfiguration.md)
  The custom object from an app built with Mac Catalyst that provides the items to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertoolbaritem/delegate)*