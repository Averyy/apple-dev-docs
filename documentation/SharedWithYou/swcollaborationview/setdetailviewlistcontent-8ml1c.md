# setDetailViewListContent(_:)

**Framework**: Shared With You  
**Kind**: method

Sets the detail view for the list content from view builder closures.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func setDetailViewListContent<ListContent>(@ViewBuilder _ detailViewListContent: () -> ListContent) where ListContent : View
```

## Parameters

- `detailViewListContent`: A   view.

## See Also

- [func setContent(UIView)](swcollaborationview/setcontent(_:).md)
  Sets the content view.
- [func setDetailViewListContent<ListContent>(ListContent)](swcollaborationview/setdetailviewlistcontent(_:)-88gy5.md)
  Sets the detail view for the list content.
- [func setShowManageButton(Bool)](swcollaborationview/setshowmanagebutton(_:).md)
  A Boolean value the system uses to show or hide the default manage-participants button in the collaboration popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/setdetailviewlistcontent(_:)-8ml1c)*