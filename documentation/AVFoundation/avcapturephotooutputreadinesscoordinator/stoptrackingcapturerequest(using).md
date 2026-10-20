# stopTrackingCaptureRequest(using:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Stop tracking the capture request represented by the specified photo setting’s unique identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func stopTrackingCaptureRequest(using settingsUniqueID: Int64)
```

```objc
- (void) stopTrackingCaptureRequestUsingPhotoSettingsUniqueID:(int64_t) settingsUniqueID;
```

## Parameters

- `settingsUniqueID`: The [`uniqueID`](../avcapturephotosettings/uniqueid.md) value of the related photo settings object.

## See Also

### Performing tracking requests
- [func startTrackingCaptureRequest(using: AVCapturePhotoSettings)](./starttrackingcapturerequest%28using%29.md)
  Tracks a capture request that uses the specified photo settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/stoptrackingcapturerequest(using:))*