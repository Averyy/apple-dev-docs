# CMMApplyTransformProc

**Framework**: ColorSync  
**Kind**: typealias  
**Role**: Type Alias

A function a CMM provider implements to apply a color transform to image data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
typealias CMMApplyTransformProc = (ColorSyncTransform?, Int, Int, Int, UnsafeMutablePointer<UnsafeMutableRawPointer>, ColorSyncDataDepth, ColorSyncDataLayout, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool
```

```c
typedef _Bool (*)(struct ColorSyncTransform *, unsigned long, unsigned long, unsigned long, void **, enum ColorSyncDataDepth, unsigned int, unsigned long, unsigned long, const void **, enum ColorSyncDataDepth, unsigned int, unsigned long, const struct __CFDictionary *) CMMApplyTransformProc;
```

## See Also

### Implementing CMM callbacks
- [typealias ColorSyncCMMIterateCallback](./colorsynccmmiteratecallback.md)
  A callback that the framework invokes for each installed CMM during iteration.
- [typealias CMMCreateTransformPropertyProc](./cmmcreatetransformpropertyproc.md)
  A function a CMM provider implements to create a transform property for a given key.
- [typealias CMMInitializeLinkProfileProc](./cmminitializelinkprofileproc.md)
  A function a CMM provider implements to initialize a device-link profile.
- [typealias CMMInitializeTransformProc](./cmminitializetransformproc.md)
  A function a CMM provider implements to initialize a color transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/cmmapplytransformproc)*