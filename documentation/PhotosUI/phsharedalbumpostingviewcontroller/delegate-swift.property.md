# delegate

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The delegate to respond to `PHSharedAlbumPostingViewController` events.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
weak var delegate: (any PHSharedAlbumPostingViewController.Delegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PHSharedAlbumPostingViewControllerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller/delegate-swift.property)*