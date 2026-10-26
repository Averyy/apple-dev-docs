# PHLivePhotoEditingErrorDomain

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

The domain value for error objects produced by a Live Photo editing context.

**Availability**:
- macOS 10.12+ - Deprecated in 10.15 (renamed: PHPhotosErrorDomain)

## Declaration

```swift
let PHLivePhotoEditingErrorDomain: String
```

```c
extern NSString * const PHLivePhotoEditingErrorDomain;
```

#### Discussion

This domain appears for errors in the completion handlers of the [`init(livePhotoEditingInput:)`](./phlivephotoeditingcontext/init%28livephotoeditinginput%29.md) and [`saveLivePhoto(to:options:completionHandler:)`](./phlivephotoeditingcontext/savelivephoto%28to,options,completionhandler%29.md) methods.

## See Also

### Errors
- [enum PHLivePhotoEditingErrorCode](./phlivephotoeditingerrorcode.md)
  Error codes for Live Photo editing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingerrordomain)*