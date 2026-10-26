# sharedAlbumPostingViewController(_:didCompleteWithError:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func sharedAlbumPostingViewController(_ postingViewController: PHSharedAlbumPostingViewController, didCompleteWithError error: (any Error)?)
```

```objc
- (void) sharedAlbumPostingViewController:(PHSharedAlbumPostingViewController *) postingViewController didCompleteWithError:(NSError *) error;
```

#### Discussion

Called when asset posting has completed.

`error` will be `nil` if asset posting was successful and non-`nil` if it was unsuccessful. The view controller won’t be dismissed automatically when this method is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller/delegate-swift.protocol/sharedalbumpostingviewcontroller(_:didcompletewitherror:))*