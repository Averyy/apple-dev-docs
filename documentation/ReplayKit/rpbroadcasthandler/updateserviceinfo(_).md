# updateServiceInfo(_:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Sends information about the current broadcast to the broadcasting app.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
func updateServiceInfo(_ serviceInfo: [String : any NSCoding & NSObjectProtocol])
```

```objc
- (void) updateServiceInfo:(NSDictionary<NSString *,NSObject<NSCoding> *> *) serviceInfo;
```

## Discussion

This method populates the [`serviceInfo`](../rpbroadcastcontroller/serviceinfo.md) property on [`RPBroadcastController`](../rpbroadcastcontroller.md) to send viewing stats or messages to the broadcasting app.

## Parameters

- `serviceInfo`: Dictionary that is passed back to the broadcasting app and contains information about the ongoing broadcast.

## See Also

### Updating Current Broadcast Information
- [func updateBroadcast(URL)](./updatebroadcast%28_%29.md)
  Sends the current broadcast URL to the broadcast controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler/updateserviceinfo(_:))*