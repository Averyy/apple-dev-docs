# devices

**Framework**: AVFoundation  
**Kind**: property

An array of external sync devices connected to this host.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var devices: [AVExternalSyncDevice] { get }
```

#### Discussion

The list is updated when external sync devices are connected to the host and they remain in the list until they become unavailable. This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession/devices)*