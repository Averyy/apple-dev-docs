# CMMInitializeLinkProfileProc

**Framework**: ColorSync  
**Kind**: typealias

A function a CMM provider implements to initialize a device-link profile.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
typealias CMMInitializeLinkProfileProc = (ColorSyncMutableProfile?, CFArray?, CFDictionary?) -> Bool
```

## See Also

- [typealias ColorSyncCMMIterateCallback](colorsynccmmiteratecallback.md)
  A callback that the framework invokes for each installed CMM during iteration.
- [typealias CMMApplyTransformProc](cmmapplytransformproc.md)
  A function a CMM provider implements to apply a color transform to image data.
- [typealias CMMCreateTransformPropertyProc](cmmcreatetransformpropertyproc.md)
  A function a CMM provider implements to create a transform property for a given key.
- [typealias CMMInitializeTransformProc](cmminitializetransformproc.md)
  A function a CMM provider implements to initialize a color transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/cmminitializelinkprofileproc)*