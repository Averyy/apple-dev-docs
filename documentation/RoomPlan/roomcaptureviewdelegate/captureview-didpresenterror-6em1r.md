# captureView(didPresent:error:)

**Framework**: RoomPlan  
**Kind**: method

Provides a default, blank implementation for the processed scan-results callback.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
func captureView(didPresent processedResult: CapturedRoom, error: (any Error)?)
```

#### Discussion

The system calls this implementation if your app doesn’t implement [`captureView(didPresent:error:)`](roomcaptureviewdelegate/captureview(didpresent:error:).md).

## Parameters

- `processedResult`: A structure that provides detailed information about the dimensions and features of the scanned room.
- `error`: An object that describes the problem when an error occurs; otherwise,  .

## See Also

- [func captureView(shouldPresent: CapturedRoomData, error: (any Error)?) -> Bool](roomcaptureviewdelegate/captureview(shouldpresent:error:)-5l74q.md)
  Indicates that the app receives and displays post-processed scan results when the scan session stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureviewdelegate/captureview(didpresent:error:)-6em1r)*