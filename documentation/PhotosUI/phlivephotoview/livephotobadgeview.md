# livePhotoBadgeView

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A view for displaying Live Photo status.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var livePhotoBadgeView: NSView? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSView * livePhotoBadgeView;
```

#### Discussion

The [`PHLivePhotoView`](../phlivephotoview.md) uses this subview to display icons indicating the existence or status of Live Photo content. Photos manages the content displayed in the badge view, so you don’t need to do anything with view’s content—instead, this property provides access to the badge view so you can change where it appears in your view hierarchy if needed. For example, if you display a Live Photo view within a scroll view, you can move the badge view so that its position remains constant while the scroll view scrolls.

## See Also

### Accessing User Interface Icons for Live Photos
- [class func livePhotoBadgeImage(options: PHLivePhotoBadgeOptions) -> UIImage](./livephotobadgeimage%28options%29.md)
  Returns an icon image for the specified Live Photo semantic options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview/livephotobadgeview)*