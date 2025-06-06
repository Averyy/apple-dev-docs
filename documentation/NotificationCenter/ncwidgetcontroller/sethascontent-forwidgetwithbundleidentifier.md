# setHasContent(_:forWidgetWithBundleIdentifier:)

**Framework**: Notification Center  
**Kind**: method

Sets whether the specified widget has content to display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+

## Declaration

```swift
func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String)
```

#### Discussion

Both a widget and its containing app can use this method to specify whether the widget has content to display. The value of `flag` determines whether a widget should be visible in the Today view and whether the widget’s most recent snapshot is still valid.

## Parameters

- `flag`: Indicates whether the widget has content to display. Default value is  .
- `bundleID`: The bundle identifier of the widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/sethascontent(_:forwidgetwithbundleidentifier:))*