# Formats

**Framework**: Avfoundation

Configure capture formats and camera frame rates.

#### Overview

The following code example illustrates how to select an iOS device’s highest possible frame rate:

```swift
func configureCameraForHighestFrameRate(device: AVCaptureDevice) {
    
    var bestFormat: AVCaptureDevice.Format?
    var bestFrameRateRange: AVFrameRateRange?

    for format in device.formats {
        for range in format.videoSupportedFrameRateRanges {
            if range.maxFrameRate > bestFrameRateRange?.maxFrameRate ?? 0 {
                bestFormat = format
                bestFrameRateRange = range
            }
        }
    }
    
    if let bestFormat = bestFormat, 
       let bestFrameRateRange = bestFrameRateRange {
        do {
            try device.lockForConfiguration()
            
            // Set the device's active format.
            device.activeFormat = bestFormat
            
            // Set the device's min/max frame duration.
            let duration = bestFrameRateRange.minFrameDuration
            device.activeVideoMinFrameDuration = duration
            device.activeVideoMaxFrameDuration = duration
            
            device.unlockForConfiguration()
        } catch {
            // Handle error.
        }
    }
}
```

Most common configurations of capture settings are available through the [`AVCaptureSession`](avcapturesession.md) object and its available presets. However, on iOS devices, some specialized options (such as high frame rate) require directly setting a capture format on an [`AVCaptureDevice`](avcapturedevice.md) instance.

> **Note**:  In iOS, directly configuring a capture device’s [`activeFormat`](avcapturedevice/activeformat.md) property changes the capture session’s preset to [`inputPriority`](avcapturesession/preset/inputpriority.md). Upon making this change, the capture session no longer automatically configures the capture format when you call the [`startRunning()`](avcapturesession/startrunning().md) method or call the [`commitConfiguration()`](avcapturesession/commitconfiguration().md) method after changing the session topology. In macOS, a capture session can still automatically configure the capture format after you make changes. To prevent automatic changes to the capture format in macOS, follow the advice listed under the [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method.

## Topics

### Configuring Capture Formats
- [var formats: [AVCaptureDevice.Format]](avcapturedevice/formats.md)
  The capture formats a device supports.
- [var activeFormat: AVCaptureDevice.Format](avcapturedevice/activeformat.md)
  The capture format in use by the device.
- [var activeDepthDataFormat: AVCaptureDevice.Format?](avcapturedevice/activedepthdataformat.md)
  The currently active depth data format of the capture device.
- [AVCaptureDevice.Format](avcapturedevice/format.md)
  A class that defines media formats and capture settings that capture devices support.
### Configuring Frame Durations
- [var activeVideoMinFrameDuration: CMTime](avcapturedevice/activevideominframeduration.md)
  The currently active minimum frame duration.
- [var activeVideoMaxFrameDuration: CMTime](avcapturedevice/activevideomaxframeduration.md)
  The currently active maximum frame duration.
- [var activeDepthDataMinFrameDuration: CMTime](avcapturedevice/activedepthdataminframeduration.md)
  The minimum frame duration of depth data.

## See Also

- [func lockForConfiguration() throws](avcapturedevice/lockforconfiguration.md)
  Requests exclusive access to configure device hardware properties.
- [func unlockForConfiguration()](avcapturedevice/unlockforconfiguration.md)
  Releases exclusive control over device hardware properties.
- [var isSubjectAreaChangeMonitoringEnabled: Bool](avcapturedevice/issubjectareachangemonitoringenabled.md)
  A Boolean value that indicates whether the device monitors the subject area for changes.
- [class let subjectAreaDidChangeNotification: NSNotification.Name](avcapturedevice/subjectareadidchangenotification.md)
  A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Focus](capture-device-focus.md)
  Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](capture-device-exposure.md)
  Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White Balance](capture-device-white-balance.md)
  Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md)
  Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capture-device-formats)*