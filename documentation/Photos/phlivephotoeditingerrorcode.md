# PHLivePhotoEditingErrorCode

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Error codes for Live Photo editing errors.

**Availability**:
- macOS 10.12+

## Declaration

```swift
enum PHLivePhotoEditingErrorCode
```

```c
enum PHLivePhotoEditingErrorCode : NSInteger;
```

## Overview

These error codes appear for errors in the completion handlers of the [`init(livePhotoEditingInput:)`](./phlivephotoeditingcontext/init%28livephotoeditinginput%29.md) and [`saveLivePhoto(to:options:completionHandler:)`](./phlivephotoeditingcontext/savelivephoto%28to,options,completionhandler%29.md) methods.

## Topics

### Constants
- [PHLivePhotoEditingErrorCode.unknown](./phlivephotoeditingerrorcode/unknown.md)
  No further information is available about the cause of the error.
- [PHLivePhotoEditingErrorCode.aborted](./phlivephotoeditingerrorcode/aborted.md)
  Live Photo processing was canceled by the Processing an Editing Context’s Live Photo method.
### Initializers
- [init?(rawValue: Int)](./phlivephotoeditingerrorcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [let PHLivePhotoEditingErrorDomain: String](./phlivephotoeditingerrordomain.md)
  The domain value for error objects produced by a Live Photo editing context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingerrorcode)*