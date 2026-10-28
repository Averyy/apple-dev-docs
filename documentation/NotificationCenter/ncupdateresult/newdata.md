# NCUpdateResult.newData

**Framework**: Notification Center  
**Kind**: case  
**Role**: Case

The update resulted in new data to display.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 8.0+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
case newData
```

```c
NCUpdateResultNewData
```

## Discussion

When new data is available, the widget might have to update its layout.

## See Also

### Constants
- [NCUpdateResult.noData](./nodata.md)
  The update did not result in any new data since the last update.
- [NCUpdateResult.failed](./failed.md)
  The update attempt failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncupdateresult/newdata)*