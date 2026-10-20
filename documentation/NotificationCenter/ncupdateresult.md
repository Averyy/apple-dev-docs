# NCUpdateResult

**Framework**: Notification Center  
**Kind**: enum  
**Role**: Enumeration

The result of updating a widget’s state.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 8.0+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
enum NCUpdateResult
```

```c
enum NCUpdateResult : NSUInteger;
```

## Topics

### Constants
- [NCUpdateResult.newData](./ncupdateresult/newdata.md)
  The update resulted in new data to display.
- [NCUpdateResult.noData](./ncupdateresult/nodata.md)
  The update did not result in any new data since the last update.
- [NCUpdateResult.failed](./ncupdateresult/failed.md)
  The update attempt failed.
### Initializers
- [init?(rawValue: UInt)](./ncupdateresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Updating a Widget’s Contents
- [func widgetPerformUpdate(completionHandler: (NCUpdateResult) -> Void)](./ncwidgetproviding/widgetperformupdate%28completionhandler%29.md)
  Called to give a widget an opportunity to update its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncupdateresult)*