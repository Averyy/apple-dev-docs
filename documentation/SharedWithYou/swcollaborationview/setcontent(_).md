# setContent(_:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Sets the content view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func setContent(_ detailViewListContentView: UIView)
```

*macOS*

```swift
func setContent(_ detailViewListContentView: NSView)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (void) setContentView:(UIView *) detailViewListContentView;
```

*macOS*

```objc
- (void) setContentView:(NSView *) detailViewListContentView;
```

## Parameters

- `detailViewListContentView`: The `NSView` for the detail view content.

## See Also

### Setting view attributes
- [func setDetailViewListContent<ListContent>(ListContent)](./setdetailviewlistcontent%28_%29-88gy5.md)
  Sets the detail view for the list content.
- [func setDetailViewListContent<ListContent>(() -> ListContent)](./setdetailviewlistcontent%28_%29-8ml1c.md)
  Sets the detail view for the list content from view builder closures.
- [func setShowManageButton(Bool)](./setshowmanagebutton%28_%29.md)
  A Boolean value the system uses to show or hide the default manage-participants button in the collaboration popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/setcontent(_:))*