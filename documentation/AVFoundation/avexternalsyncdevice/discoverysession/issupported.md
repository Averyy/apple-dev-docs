# isSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Whether external sync devices are supported by this device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class var isSupported: Bool { get }
```

```objc
@property (class, readonly, getter=isSupported) BOOL supported;
```

## Discussion

A value of `true` indicates that external sync devices are supported while `false` indicates they are not.

## See Also

### Accessing the shared instance
- [class var shared: AVExternalSyncDevice.DiscoverySession?](./shared.md)
  The singleton instance of the external sync source device discovery session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession/issupported)*