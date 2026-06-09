# sendData(_:toApplication:session:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called when an app sends data to a remote application.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func sendData(_ data: Data, toApplication applicationIdentifier: String, session: MediaOutputSession)
```

#### Discussion

In the case of media-app to remote media-application communication, the media-application’s specific application identifier will be used.

In the case of media-app to media device extension communication, the following application identifier will be used: `com.apple.media-device-extension`.

## Parameters

- `data`: The data to send to the remote application.
- `applicationIdentifier`: The identifier of the target application.
- `session`: The session associated with the data transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/senddata(_:toapplication:session:))*