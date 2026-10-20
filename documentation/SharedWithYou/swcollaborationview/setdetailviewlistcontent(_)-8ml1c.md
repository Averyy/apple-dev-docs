# setDetailViewListContent(_:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Sets the detail view for the list content from view builder closures.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func setDetailViewListContent<ListContent>(@ViewBuilder _ detailViewListContent: () -> ListContent) where ListContent : View
```

## Parameters

- `detailViewListContent`: A `ListContent` view.

## See Also

### Setting view attributes
- [func setContent(UIView)](./setcontent%28_%29.md)
  Sets the content view.
- [func setDetailViewListContent<ListContent>(ListContent)](./setdetailviewlistcontent%28_%29-88gy5.md)
  Sets the detail view for the list content.
- [func setShowManageButton(Bool)](./setshowmanagebutton%28_%29.md)
  A Boolean value the system uses to show or hide the default manage-participants button in the collaboration popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/setdetailviewlistcontent(_:)-8ml1c)*