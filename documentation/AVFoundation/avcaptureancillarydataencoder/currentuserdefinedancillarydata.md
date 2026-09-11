# currentUserDefinedAncillaryData

**Framework**: AVFoundation  
**Kind**: property

This is a representation of the user defined anacillary data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var currentUserDefinedAncillaryData: [AVCaptureAncillaryDataUserKey : Any] { get }
```

#### Discussion

Using SMPTE 291 and SMPTE RDD 18 standards for user-defined data, this property specifies the user-defined ancillary data to be sent with every frame in [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md).  The dictionary will contain a NSUUID the [`rdd18InstanceUID`](avcaptureancillarydatauserkey/rdd18instanceuid.md) key, a uint16_t for the [`rdd18UDAMSetVersion`](avcaptureancillarydatauserkey/rdd18udamsetversion.md) key and a dictionary for the [`rdd18UserItems`](avcaptureancillarydatauserkey/rdd18useritems.md). The [`rdd18UserItems`](avcaptureancillarydatauserkey/rdd18useritems.md) will contain keys of the user tag and with the corresponding values.

To update the data please see the following methods:

- `setUserInstanceUID:userUdamVersion:` will update the [`rdd18InstanceUID`](avcaptureancillarydatauserkey/rdd18instanceuid.md) and [`rdd18UDAMSetVersion`](avcaptureancillarydatauserkey/rdd18udamsetversion.md) keys
- [`setRDD18AncillaryData(_:forTag:)`](avcaptureancillarydataencoder/setrdd18ancillarydata(_:fortag:).md)  will update the [`rdd18UserItems`](avcaptureancillarydatauserkey/rdd18useritems.md) key
- [`setRDD18AncillaryDataString(_:forTag:)`](avcaptureancillarydataencoder/setrdd18ancillarydatastring(_:fortag:).md) will update the [`rdd18UserItems`](avcaptureancillarydatauserkey/rdd18useritems.md) key


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureancillarydataencoder/currentuserdefinedancillarydata)*