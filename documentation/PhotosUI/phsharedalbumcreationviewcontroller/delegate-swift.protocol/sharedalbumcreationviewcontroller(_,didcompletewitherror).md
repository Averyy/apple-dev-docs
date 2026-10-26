# sharedAlbumCreationViewController(_:didCompleteWithError:)

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
func sharedAlbumCreationViewController(_ creationViewController: PHSharedAlbumCreationViewController, didCompleteWithError error: (any Error)?)
```

```objc
- (void) sharedAlbumCreationViewController:(PHSharedAlbumCreationViewController *) creationViewController didCompleteWithError:(NSError *) error;
```

#### Discussion

Called when shared album creation completes.

If creation was successful, `-[PHSharedAlbumCreationViewController albumIdentifier]` will be non-`nil` and `error` will be `nil`. If creation was unsuccessful, `-[PHSharedAlbumCreationViewController albumIdentifier]` will be `nil` and `error` will be non-`nil`. The creation was cancelled by the user, both `-[PHSharedAlbumCreationViewController albumIdentifier]` and `error` will be `nil`. The view controller won’t be dismissed automatically when this method is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcreationviewcontroller/delegate-swift.protocol/sharedalbumcreationviewcontroller(_:didcompletewitherror:))*