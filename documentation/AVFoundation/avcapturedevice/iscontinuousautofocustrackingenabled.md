# isContinuousAutoFocusTrackingEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the device should use continuous autofocus tracking.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isContinuousAutoFocusTrackingEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isContinuousAutoFocusTrackingEnabled) BOOL continuousAutoFocusTrackingEnabled;
```

#### Discussion

The default value for this property is `false`. On a device with an active format where `isContinuousAutoFocusTrackingSupported` returns `true` and [`isContinuousAutoFocusTrackingEnabled`](./iscontinuousautofocustrackingenabled.md) is set to `true`, continuous autofocus tracking will be engaged when the device’s focus mode is set to `AVCaptureFocusModeContinuousAutoFocus`. When engaged, the subject at the current [`focusPointOfInterest`](./focuspointofinterest.md) will be tracked as it moves within the scene and will be kept in focus automatically. The device’s [`isContinuousAutoFocusTrackingSubjectAcquired`](./iscontinuousautofocustrackingsubjectacquired.md) property will return `true` while any tracked subject remains in the scene. However, the device’s [`focusPointOfInterest`](./focuspointofinterest.md) and [`focusRectOfInterest`](./focusrectofinterest.md) are not updated while continuous autofocus tracking is active. Continuous autofocus tracking can be made inactive by setting [`isContinuousAutoFocusTrackingEnabled`](./iscontinuousautofocustrackingenabled.md) to `false` and then setting the device’s focus mode to `AVCaptureFocusModeContinuousAutoFocus` or by setting the focus mode to a value other than `AVCaptureFocusModeContinuousAutoFocus`. When made inactive, [`isContinuousAutoFocusTrackingSubjectAcquired`](./iscontinuousautofocustrackingsubjectacquired.md) changes to `false`, as no subject is being tracked. For virtual cameras, continuous autofocus tracking only works on the [`activePrimaryConstituent`](./activeprimaryconstituent.md).

To receive continuous autofocus tracking updates, it is required to connect this device to an [`AVCaptureMetadataOutput`](../avcapturemetadataoutput.md) that is configured to deliver [`focusTrackedObject`](../avmetadataobject/objecttype/focustrackedobject.md). If [`focusTrackedObject`](../avmetadataobject/objecttype/focustrackedobject.md) is not subscribed, no updates will be provided for continuous autofocus tracking and the device’s [`isContinuousAutoFocusTrackingSubjectAcquired`](./iscontinuousautofocustrackingsubjectacquired.md) property remains to be `false`.

> **Throws**: `NSInvalidArgumentException` if this property is set to `true` when the active format’s `isContinuousAutoFocusTrackingSupported` returns `false`.

> **Throws**: `NSInvalidArgumentException` if this property is set to `true` when the device is configured for cinematic video capture.

> **Throws**: `NSGenericException` if the device is not locked for configuration using [`lockForConfiguration()`](./lockforconfiguration%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscontinuousautofocustrackingenabled)*