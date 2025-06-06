# NCUpdateResult

**Framework**: Notification Center  
**Kind**: enum

The result of updating a widget’s state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+

## Declaration

```swift
enum NCUpdateResult
```

## Topics

### Constants
- [NCUpdateResult.newData](ncupdateresult/newdata.md)
  The update resulted in new data to display.
- [NCUpdateResult.noData](ncupdateresult/nodata.md)
  The update did not result in any new data since the last update.
- [NCUpdateResult.failed](ncupdateresult/failed.md)
  The update attempt failed.
### Initializers
- [init?(rawValue: UInt)](ncupdateresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func widgetPerformUpdate(completionHandler: (NCUpdateResult) -> Void)](ncwidgetproviding/widgetperformupdate(completionhandler:).md)
  Called to give a widget an opportunity to update its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncupdateresult)*