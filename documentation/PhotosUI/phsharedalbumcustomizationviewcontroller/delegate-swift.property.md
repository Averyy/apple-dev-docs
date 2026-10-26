# delegate

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The delegate to respond to `PHSharedAlbumCustomizationViewController` events.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
weak var delegate: (any PHSharedAlbumCustomizationViewController.Delegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PHSharedAlbumCustomizationViewControllerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller/delegate-swift.property)*