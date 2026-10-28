# setHasContent(_:forWidgetWithBundleIdentifier:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Sets whether the specified widget has content to display.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 8.0+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String)
```

```objc
- (void) setHasContent:(BOOL) flag forWidgetWithBundleIdentifier:(NSString *) bundleID;
```

## Discussion

Both a widget and its containing app can use this method to specify whether the widget has content to display. The value of `flag` determines whether a widget should be visible in the Today view and whether the widget’s most recent snapshot is still valid.

## Parameters

- `flag`: Indicates whether the widget has content to display. Default value is [`true`](../../Swift/true.md).
- `bundleID`: The bundle identifier of the widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/sethascontent(_:forwidgetwithbundleidentifier:))*