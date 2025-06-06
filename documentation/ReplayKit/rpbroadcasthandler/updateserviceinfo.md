# updateServiceInfo(_:)

**Framework**: ReplayKit  
**Kind**: method

Sends information about the current broadcast to the broadcasting app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func updateServiceInfo(_ serviceInfo: [String : any NSCoding & NSObjectProtocol])
```

#### Discussion

This method populates the [`serviceInfo`](rpbroadcastcontroller/serviceinfo.md) property on [`RPBroadcastController`](rpbroadcastcontroller.md) to send viewing stats or messages to the broadcasting app.

## Parameters

- `serviceInfo`: Dictionary that is passed back to the broadcasting app and contains information about the ongoing broadcast.

## See Also

- [func updateBroadcast(URL)](rpbroadcasthandler/updatebroadcast(_:).md)
  Sends the current broadcast URL to the broadcast controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler/updateserviceinfo(_:))*