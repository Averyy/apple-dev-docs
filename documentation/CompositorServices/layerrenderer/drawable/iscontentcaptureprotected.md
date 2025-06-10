# isContentCaptureProtected

**Framework**: Compositor Services  
**Kind**: property

Returns whether content capture is protected and it is safe to draw content that should be protected from capture.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var isContentCaptureProtected: Bool { get }
```

#### Discussion

Use this function to ensure that drawing that is only meant for eyes in the device is not drawn when false. Only adopt if app has adopted SwiftUI `activatesContentCaptureProtected` scene modifier and drawing will have content that is not desired to meant to be captured. For `cp_drawable_target_capture` this will always return false as it is upto the renderer to handle drawing content that will be captured beyond the built-in displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/iscontentcaptureprotected)*