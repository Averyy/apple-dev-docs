# shared

**Framework**: AVFoundation  
**Kind**: property

The singleton instance of the external sync source device discovery session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class var shared: AVExternalSyncDevice.DiscoverySession? { get }
```

#### Discussion

Access the one and only external sync device discovery session on this host device using this method. `sharedSession` returns `nil` if the host device doesn’t support external sync devices.

## See Also

- [class var isSupported: Bool](avexternalsyncdevice/discoverysession/issupported.md)
  Whether external sync devices are supported by this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession/shared)*