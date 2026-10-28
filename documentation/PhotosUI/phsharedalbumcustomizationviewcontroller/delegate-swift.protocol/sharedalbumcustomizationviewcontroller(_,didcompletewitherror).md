# sharedAlbumCustomizationViewController(_:didCompleteWithError:)

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
func sharedAlbumCustomizationViewController(_ customizationViewController: PHSharedAlbumCustomizationViewController, didCompleteWithError error: (any Error)?)
```

```objc
- (void) sharedAlbumCustomizationViewController:(PHSharedAlbumCustomizationViewController *) customizationViewController didCompleteWithError:(NSError *) error;
```

## Discussion

Called when shared album customization completes.

`error` will be `nil` if customization was successful and non-`nil` if it was unsuccessful. The view controller won’t be dismissed automatically when this method is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller/delegate-swift.protocol/sharedalbumcustomizationviewcontroller(_:didcompletewitherror:))*