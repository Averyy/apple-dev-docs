# captureView(shouldPresent:error:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates whether the app processes raw scan results immediately after a scan session stops.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureView(shouldPresent roomDataForProcessing: CapturedRoomData, error: (any Error)?) -> Bool
```

#### Return Value

A Boolean value that determines whether the app receives and displays post-processed scan results when the scan session stops.

#### Discussion

If your app returns `true`:

- The framework processes the scan results immediately and calls [`captureView(didPresent:error:)`](./captureview%28didpresent,error%29.md).
- The view ([`RoomCaptureView`](../roomcaptureview.md)) displays the scanned room in a 3D rendition that the user can inspect using touch gestures. The user can view the room from different angles by panning, pinching, or expanding. After inspecting the scanned room, the user can decide whether to export the room to a file or whether to begin another scan.

To omit processing, return `false`. You can save the raw scan results (`roomDataForProcessing`) to an encoder for processing at a later date or send the raw data to a server for processing on a different device.

The default implementation returns `true`.

## Parameters

- `roomDataForProcessing`: A data object that contains the raw scan results.
- `error`: An object that describes the problem when an error occurs; otherwise, `nil`.

## Default Implementations

### RoomCaptureViewDelegate Implementations
- [func captureView(shouldPresent: CapturedRoomData, error: (any Error)?) -> Bool](./captureview%28shouldpresent,error%29-5l74q.md)
  Indicates that the app receives and displays post-processed scan results when the scan session stops.

## See Also

### Post-processing scan results
- [func captureView(didPresent: CapturedRoom, error: (any Error)?)](./captureview%28didpresent,error%29.md)
  Provides the delegate with the processed scan results as the view presents them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureviewdelegate/captureview(shouldpresent:error:))*