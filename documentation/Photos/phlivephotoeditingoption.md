# PHLivePhotoEditingOption

**Framework**: Photos  
**Kind**: struct  
**Role**: Structure

Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct PHLivePhotoEditingOption
```

```c
typedef NSString * const PHLivePhotoEditingOption;
```

## Topics

### Initializers
- [init(rawValue: String)](./phlivephotoeditingoption/init%28rawvalue%29.md)
  Initializes a Live Photo editing option from its raw value.
### Type Properties
- [static let shouldRenderAtPlaybackTime: PHLivePhotoEditingOption](./phlivephotoeditingoption/shouldrenderatplaybacktime.md)
  Specifies whether processing should occur during or before playback.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Processing an Editing Context’s Live Photo
- [func saveLivePhoto(to: PHContentEditingOutput, options: [String : Any]?, completionHandler: (Bool, (any Error)?) -> Void)](./phlivephotoeditingcontext/savelivephoto%28to,options,completionhandler%29.md)
  Processes and saves a full-quality Live Photo as the output of your editing session.
- [func prepareLivePhotoForPlayback(withTargetSize: CGSize, options: [String : Any]?, completionHandler: (PHLivePhoto?, (any Error)?) -> Void)](./phlivephotoeditingcontext/preparelivephotoforplayback%28withtargetsize,options,completionhandler%29.md)
  Processes a Live Photo with your edits for viewing.
- [func cancel()](./phlivephotoeditingcontext/cancel%28%29.md)
  Aborts any Live Photo processing in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingoption)*