# CMMCreateTransformPropertyProc

**Framework**: ColorSync  
**Kind**: typealias

A function a CMM provider implements to create a transform property for a given key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
typealias CMMCreateTransformPropertyProc = (ColorSyncTransform?, CFTypeRef?, CFDictionary?) -> Unmanaged<CFTypeRef>?
```

## See Also

- [typealias ColorSyncCMMIterateCallback](colorsynccmmiteratecallback.md)
  A callback that the framework invokes for each installed CMM during iteration.
- [typealias CMMApplyTransformProc](cmmapplytransformproc.md)
  A function a CMM provider implements to apply a color transform to image data.
- [typealias CMMInitializeLinkProfileProc](cmminitializelinkprofileproc.md)
  A function a CMM provider implements to initialize a device-link profile.
- [typealias CMMInitializeTransformProc](cmminitializetransformproc.md)
  A function a CMM provider implements to initialize a color transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/cmmcreatetransformpropertyproc)*