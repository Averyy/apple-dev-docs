# ColorSyncCMMIterateCallback

**Framework**: ColorSync  
**Kind**: typealias

A callback that the framework invokes for each installed CMM during iteration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
typealias ColorSyncCMMIterateCallback = (ColorSyncCMM?, UnsafeMutableRawPointer?) -> Bool
```

#### Discussion

Return `false` to stop the iteration.

## Parameters

- `cmm`: The CMM for this iteration step.
- `userInfo`: The user info passed to the iteration function.

## See Also

- [typealias CMMApplyTransformProc](cmmapplytransformproc.md)
  A function a CMM provider implements to apply a color transform to image data.
- [typealias CMMCreateTransformPropertyProc](cmmcreatetransformpropertyproc.md)
  A function a CMM provider implements to create a transform property for a given key.
- [typealias CMMInitializeLinkProfileProc](cmminitializelinkprofileproc.md)
  A function a CMM provider implements to initialize a device-link profile.
- [typealias CMMInitializeTransformProc](cmminitializetransformproc.md)
  A function a CMM provider implements to initialize a color transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynccmmiteratecallback)*