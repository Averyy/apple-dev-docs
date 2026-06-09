# startSession(_:identifier:url:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called when media playback or a remote application should be started on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func startSession(_ session: MediaOutputSession, identifier: String?, url: URL)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

## Parameters

- `session`: The session associated with the playback request.
- `identifier`: The application identifier for the remote application. If `nil`, the extension should provide a default media playback experience on the remote device.
- `url`: The URL identifying the media content or application specific URL for the remote application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/startsession(_:identifier:url:))*