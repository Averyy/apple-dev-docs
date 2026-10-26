# saveLivePhoto(to:options:completionHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Processes and saves a full-quality Live Photo as the output of your editing session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func saveLivePhoto(to output: PHContentEditingOutput, options: [String : Any]? = nil, completionHandler handler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func saveLivePhoto(to output: PHContentEditingOutput, options: [String : Any]? = nil) async throws
```

```objc
- (void) saveLivePhotoToOutput:(PHContentEditingOutput *) output options:(NSDictionary<NSString *,id> *) options completionHandler:(void (^)(BOOL success, NSError *error)) handler;
```

#### Discussion

Use this method when you have finished an editing session and need to provide rendered output in a [`PHContentEditingOutput`](../phcontenteditingoutput.md) object. Unlike when rendering output for a photo or video asset, you don’t need to provide rendered output using the [`renderedContentURL`](../phcontenteditingoutput/renderedcontenturl.md) property of the editing output object. Instead, create a [`PHContentEditingOutput`](../phcontenteditingoutput.md) object using the [`init(contentEditingInput:)`](../phcontenteditingoutput/init%28contenteditinginput%29.md) initializer, passing the same [`PHContentEditingInput`](../phcontenteditinginput.md) object you used in the [`PHLivePhotoFrameProcessingBlock`](../phlivephotoframeprocessingblock.md) initializer to start this Live Photo editing context. Then pass that editing output object to this method, and Photos renders the Live Photo and provides it to the editing output.

> **Note**:  Don’t forget to describe your edits in a [`PHAdjustmentData`](../phadjustmentdata.md) object and provide that to the [`adjustmentData`](../phcontenteditingoutput/adjustmentdata.md) property of your content editing output. Providing adjustment data allows your app (or photo editing extension) to non-destructively resume working with an edit later, whether on the same device or on another Mac or iOS device using iCloud Photo Library.

After this method’s completion handler signals successful rendering, you use the content editing output to complete the edit. In an app using the Photos framework, create a [`PHAssetChangeRequest`](../phassetchangerequest.md) object inside a [`PHPhotoLibrary`](../phphotolibrary.md) `performChanges` block, and set its [`contentEditingOutput`](../phassetchangerequest/contenteditingoutput.md) property to your editing output. In a photo editing extension running in the Photos app, your main view controller provides content editing output when requested by the [`finishContentEditing(completionHandler:)`](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/finishcontentediting(completionhandler:)) method.

## Parameters

- `output`: The photo editing output to receive the rendered Live Photo, created from the same [`PHContentEditingInput`](../phcontenteditinginput.md) object you used to begin this Live Photo editing context.
- `options`: Options that affect Live Photo rendering. See `Live Photo Processing Options`.
- `handler`: A block that Photos calls on the main queue after rendering is complete. The block takes the following parameters:

  - **success**: `true` if rendering succeeds; otherwise `false`.
  - **error**: If rendering succeeds, this parameter is `nil`. If rendering fails, this parameter contains an error object describing the failure.

## See Also

### Processing an Editing Context’s Live Photo
- [func prepareLivePhotoForPlayback(withTargetSize: CGSize, options: [String : Any]?, completionHandler: (PHLivePhoto?, (any Error)?) -> Void)](./preparelivephotoforplayback%28withtargetsize,options,completionhandler%29.md)
  Processes a Live Photo with your edits for viewing.
- [struct PHLivePhotoEditingOption](../phlivephotoeditingoption.md)
  Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.
- [func cancel()](./cancel%28%29.md)
  Aborts any Live Photo processing in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/savelivephoto(to:options:completionhandler:))*