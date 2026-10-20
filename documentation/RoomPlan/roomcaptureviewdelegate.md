# RoomCaptureViewDelegate

**Framework**: RoomPlan  
**Kind**: protocol  
**Role**: Protocol

A specification to post-process the results of a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
protocol RoomCaptureViewDelegate : NSCoding
```

#### Overview

The room-capture view’s delegate property ([`delegate`](./roomcaptureview/delegate.md)) is of this type.

When your app scans a room using the framework-provided view ([`RoomCaptureView`](./roomcaptureview.md)), your delegate receives the raw scan results through the `roomDataForProcessing` argument of [`captureView(shouldPresent:error:)`](./roomcaptureviewdelegate/captureview%28shouldpresent,error%29.md).

If your app returns `true` to [`captureView(shouldPresent:error:)`](./roomcaptureviewdelegate/captureview%28shouldpresent,error%29.md), the framework processes the raw results and calls [`captureView(didPresent:error:)`](./roomcaptureviewdelegate/captureview%28didpresent,error%29.md) when processing completes.

## Topics

### Post-processing scan results
- [func captureView(shouldPresent: CapturedRoomData, error: (any Error)?) -> Bool](./roomcaptureviewdelegate/captureview%28shouldpresent,error%29.md)
  Indicates whether the app processes raw scan results immediately after a scan session stops.
- [func captureView(didPresent: CapturedRoom, error: (any Error)?)](./roomcaptureviewdelegate/captureview%28didpresent,error%29.md)
  Provides the delegate with the processed scan results as the view presents them.
### Default implementations
- [func captureView(shouldPresent: CapturedRoomData, error: (any Error)?) -> Bool](./roomcaptureviewdelegate/captureview%28shouldpresent,error%29-5l74q.md)
  Indicates that the app receives and displays post-processed scan results when the scan session stops.
- [func captureView(didPresent: CapturedRoom, error: (any Error)?)](./roomcaptureviewdelegate/captureview%28didpresent,error%29-6em1r.md)
  Provides a default, blank implementation for the processed scan-results callback.

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)

## See Also

### User Interface
- [class RoomCaptureView](./roomcaptureview.md)
  A view that enables the user to scan their room with the device’s camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureviewdelegate)*