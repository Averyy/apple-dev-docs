# dataSource

**Framework**: Messages  
**Kind**: property

The sticker browser’s data source.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var dataSource: (any MSStickerBrowserViewDataSource)? { get set }
```

#### Discussion

If you are using an [`MSStickerBrowserViewController`](msstickerbrowserviewcontroller.md) object, the controller automatically sets itself as the data source for the sticker browser view that it provides. If you instantiate and display your own sticker browser view, this property defaults to `nil`, and you must assign a data source.

## See Also

- [protocol MSStickerBrowserViewDataSource](msstickerbrowserviewdatasource.md)
  The protocol for dynamically providing stickers to a browser view.
- [func reloadData()](msstickerbrowserview/reloaddata.md)
  Asks the sticker browser to reload its data from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/datasource)*