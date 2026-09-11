# isContinuousAutoFocusTrackingSubjectAcquired

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the device is actively tracking a subject in the scene to maintain focus.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isContinuousAutoFocusTrackingSubjectAcquired: Bool { get }
```

#### Discussion

Returns `true` when the capture device is actively tracking a subject in the scene, and `false` otherwise. The subject is initially identified by [`focusPointOfInterest`](avcapturedevice/focuspointofinterest.md) when focus mode is set to `AVCaptureFocusModeContinuousAutoFocus` with [`isContinuousAutoFocusTrackingEnabled`](avcapturedevice/iscontinuousautofocustrackingenabled.md) set to `true`. This property is key-value observable and reflects only whether a subject is actively tracked, not which one. To identify the tracked subject, include [`focusTrackedObject`](avmetadataobject/objecttype/focustrackedobject.md) in the `metadataObjectTypes` of [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md). The [`AVMetadataFocusTrackedObject`](avmetadatafocustrackedobject.md) delivered by the metadata output represents the subject currently tracked for continuous autofocus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscontinuousautofocustrackingsubjectacquired)*