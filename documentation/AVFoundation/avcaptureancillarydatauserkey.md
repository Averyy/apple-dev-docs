# AVCaptureAncillaryDataUserKey

**Framework**: AVFoundation  
**Kind**: struct

Clients may use an AVCaptureAncillaryDataUserKey to inspect the [`currentUserDefinedAncillaryData`](avcaptureancillarydataencoder/currentuserdefinedancillarydata.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
struct AVCaptureAncillaryDataUserKey
```

## Topics

### Creating a user key
- [init(rawValue: String)](avcaptureancillarydatauserkey/init(rawvalue:).md)
### Type Properties
- [static let rdd18InstanceUID: AVCaptureAncillaryDataUserKey](avcaptureancillarydatauserkey/rdd18instanceuid.md)
  An AVCaptureAncillaryDataEncoder key corresponding with the optional RDD18 user defined metadata Instance UID
- [static let rdd18UDAMSetVersion: AVCaptureAncillaryDataUserKey](avcaptureancillarydatauserkey/rdd18udamsetversion.md)
  An AVCaptureAncillaryDataEncoder key corresponding with the optional RDD18 user defined metadata UDAM Set Version
- [static let rdd18UserItems: AVCaptureAncillaryDataUserKey](avcaptureancillarydatauserkey/rdd18useritems.md)
  An AVCaptureAncillaryDataEncoder key corresponding with RDD18 user defined metadata

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md)
  [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md) is a subclass of [`AVCaptureOutput`](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode)
- [protocol AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
- [class AVCaptureAncillaryDataEncoder](avcaptureancillarydataencoder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureancillarydatauserkey)*