# captureView(didPresent:error:)

**Framework**: RoomPlan  
**Kind**: method  
**Required**: Yes

Provides the delegate with the processed scan results as the view presents them.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
func captureView(didPresent processedResult: CapturedRoom, error: (any Error)?)
```

#### Discussion

The framework invokes this callback when your app returns `true` for [`captureView(shouldPresent:error:)`](roomcaptureviewdelegate/captureview(shouldpresent:error:).md).

With the `processedResult` argument, your app can alter the detailed captured room object or export it to a USDZ file.

## Parameters

- `processedResult`: A structure that provides detailed information about the dimensions and features of the scanned room.
- `error`: An object that describes the problem when an error occurs; otherwise,  .

## See Also

- [func captureView(shouldPresent: CapturedRoomData, error: (any Error)?) -> Bool](roomcaptureviewdelegate/captureview(shouldpresent:error:).md)
  Indicates whether the app processes raw scan results immediately after a scan session stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureviewdelegate/captureview(didpresent:error:))*