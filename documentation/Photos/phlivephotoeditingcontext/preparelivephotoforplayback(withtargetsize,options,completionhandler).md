# prepareLivePhotoForPlayback(withTargetSize:options:completionHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Processes a Live Photo with your edits for viewing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func prepareLivePhotoForPlayback(withTargetSize targetSize: CGSize, options: [String : Any]? = nil, completionHandler handler: @escaping @Sendable (PHLivePhoto?, (any Error)?) -> Void)
```

```swift
func livePhotoForPlayback(targetSize: CGSize, options: [String : Any]? = nil) async throws -> PHLivePhoto
```

```objc
- (void) prepareLivePhotoForPlaybackWithTargetSize:(CGSize) targetSize options:(NSDictionary<NSString *,id> *) options completionHandler:(void (^)(PHLivePhoto *livePhoto, NSError *error)) handler;
```

#### Discussion

Use this method to generate preview versions of the edited Live Photo—for example, to display in your editing UI.

> **Note**:  This method does not guarantee performance appropriate for interactive editing. Instead, you might preview edits interactively using a still image (see the [`fullSizeImage`](./fullsizeimage.md) property), and use this method to produce animated reviews upon the user’s request.

## Parameters

- `targetSize`: The size of the view in which you plan to preview the edited Live Photo output.
- `options`: Options that affect Live Photo rendering. See `Live Photo Processing Options`.
- `handler`: A block that Photos calls on the main queue after processing is complete. The block takes the following parameters:

  - **livePhoto**: The rendered Live Photo, suitable for displaying in a [`PHLivePhotoView`](https://developer.apple.com/documentation/photosui/phlivephotoview) object.
  - **error**: If preparing the edited Live Photo for display succeeds, this parameter is `nil`. If processing fails, the `livePhoto` parameter is `nil`, and this parameter contains an error object describing the failure.

## See Also

### Processing an Editing Context’s Live Photo
- [func saveLivePhoto(to: PHContentEditingOutput, options: [String : Any]?, completionHandler: (Bool, (any Error)?) -> Void)](./savelivephoto%28to,options,completionhandler%29.md)
  Processes and saves a full-quality Live Photo as the output of your editing session.
- [struct PHLivePhotoEditingOption](../phlivephotoeditingoption.md)
  Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.
- [func cancel()](./cancel%28%29.md)
  Aborts any Live Photo processing in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/preparelivephotoforplayback(withtargetsize:options:completionhandler:))*