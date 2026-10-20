# NSUserActivityTypeLockedCameraCapture

**Framework**: LockedCameraCapture  
**Kind**: var  
**Role**: Global Variable

A type to use when opening your app from the capture extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
let NSUserActivityTypeLockedCameraCapture: String
```

```c
extern NSString * const NSUserActivityTypeLockedCameraCapture;
```

#### Discussion

Use this `NSUserActivityType` with [`openApplication(for:)`](./lockedcameracapturesession/openapplication%28for%29.md) to check if someone is launching your app from a locked camera capture extension.

## See Also

### App integration
- [class LockedCameraCaptureManager](./lockedcameracapturemanager.md)
  An object that provides handling of captured content and transitioning to the extension’s containing app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/nsuseractivitytypelockedcameracapture)*