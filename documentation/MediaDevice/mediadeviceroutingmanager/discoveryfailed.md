# discoveryFailed(_:)

**Framework**: Media Device  
**Kind**: method

Reports a discovery failure to the system, indicating that the extension was unable to search for devices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func discoveryFailed(_ error: MediaDeviceError)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when discovery is prevented in an unexpected way. Do not call this function when devices are simply not discovered.

## Parameters

- `error`: The error describing why discovery failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/discoveryfailed(_:))*