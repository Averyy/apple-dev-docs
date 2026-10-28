# cancel()

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Aborts any Live Photo processing in progress.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

## Discussion

This method applies only after you’ve begun processing a Live Photo for display or output with the [`init(livePhotoEditingInput:)`](./init%28livephotoeditinginput%29.md) or [`saveLivePhoto(to:options:completionHandler:)`](./savelivephoto%28to,options,completionhandler%29.md) method. After you call this method, Photos calls your completion handler and provides an error with the [`PHLivePhotoEditingErrorCode.aborted`](../phlivephotoeditingerrorcode/aborted.md) error code.

## See Also

### Processing an Editing Context’s Live Photo
- [func saveLivePhoto(to: PHContentEditingOutput, options: [String : Any]?, completionHandler: (Bool, (any Error)?) -> Void)](./savelivephoto%28to,options,completionhandler%29.md)
  Processes and saves a full-quality Live Photo as the output of your editing session.
- [func prepareLivePhotoForPlayback(withTargetSize: CGSize, options: [String : Any]?, completionHandler: (PHLivePhoto?, (any Error)?) -> Void)](./preparelivephotoforplayback%28withtargetsize,options,completionhandler%29.md)
  Processes a Live Photo with your edits for viewing.
- [struct PHLivePhotoEditingOption](../phlivephotoeditingoption.md)
  Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/cancel())*