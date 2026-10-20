# captureView(shouldPresent:error:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Indicates that the app receives and displays post-processed scan results when the scan session stops.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureView(shouldPresent roomDataForProcessing: CapturedRoomData, error: (any Error)?) -> Bool
```

#### Return Value

This implementation always returns `true`.

#### Discussion

If your app’s room-capture view [`delegate`](../roomcaptureview/delegate.md) doesn’t implement [`captureView(shouldPresent:error:)`](./captureview%28shouldpresent,error%29.md), then the framework calls this default implementation.

## Parameters

- `roomDataForProcessing`: A data object that contains the raw scan results.
- `error`: An object that describes the problem when an error occurs; otherwise, `nil`.

## See Also

### Default implementations
- [func captureView(didPresent: CapturedRoom, error: (any Error)?)](./captureview%28didpresent,error%29-6em1r.md)
  Provides a default, blank implementation for the processed scan-results callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureviewdelegate/captureview(shouldpresent:error:)-5l74q)*