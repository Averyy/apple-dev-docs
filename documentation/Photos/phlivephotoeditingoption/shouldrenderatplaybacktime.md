# shouldRenderAtPlaybackTime

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

Specifies whether processing should occur during or before playback.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let shouldRenderAtPlaybackTime: PHLivePhotoEditingOption
```

```c
extern PHLivePhotoEditingOption PHLivePhotoShouldRenderAtPlaybackTime;
```

#### Discussion

The value for this key is an NSNumber object with a Boolean value. With the default value of `false`, Photos always renders your edits immediately when you call the [`init(livePhotoEditingInput:)`](../phlivephotoeditingcontext/init%28livephotoeditinginput%29.md) method, calling your [`frameProcessor`](../phlivephotoeditingcontext/frameprocessor.md) block for each frame in the Live Photo’s video and still photo content.

When you specify a value of `true`, Photos can defer rendering until playback time, calling your [`frameProcessor`](../phlivephotoeditingcontext/frameprocessor.md) block only for photo and video frames that need to be displayed. However, in this case Photos may still choose to pre-render your edits if needed.

This option does not apply when rendering for output with the [`saveLivePhoto(to:options:completionHandler:)`](../phlivephotoeditingcontext/savelivephoto%28to,options,completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingoption/shouldrenderatplaybacktime)*