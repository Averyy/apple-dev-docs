# AVCaptureAncillaryDataEncoder

**Framework**: AVFoundation  
**Kind**: class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class AVCaptureAncillaryDataEncoder
```

##### Inspecting the User Defined Data

- [`currentUserDefinedAncillaryData`](avcaptureancillarydataencoder/currentuserdefinedancillarydata.md)

## Topics

### Instance Properties
- [var currentUserDefinedAncillaryData: [AVCaptureAncillaryDataUserKey : Any]](avcaptureancillarydataencoder/currentuserdefinedancillarydata.md)
  This is a representation of the user defined anacillary data.
- [var isEnabled: Bool](avcaptureancillarydataencoder/isenabled.md)
  Indicates whether ancillary data should be encoded and transmitted.
- [var userDefinedAncillaryDataSizeRemaining: Int16](avcaptureancillarydataencoder/userdefinedancillarydatasizeremaining.md)
  Allows users to track how much data in bytes can be added to the userDefinedAncillaryData.
### Instance Methods
- [func removeRDD18AncillaryData(forTag: UInt16)](avcaptureancillarydataencoder/removerdd18ancillarydata(fortag:).md)
  Allows the user to remove the ancillary data associated with the tag.
- [func setRDD18AncillaryData(Data, forTag: UInt16) throws](avcaptureancillarydataencoder/setrdd18ancillarydata(_:fortag:).md)
  Allows the user to add their own data to be encoded and transmitted using SMPTE RDD 18 standards.
- [func setRDD18AncillaryDataString(String, forTag: UInt16) throws](avcaptureancillarydataencoder/setrdd18ancillarydatastring(_:fortag:).md)
  Allows the user to add their own string to be encoded as data and transmitted using SMPTE RDD 18 standards.
- [func setUserInstanceUID(UUID, forUserUDAMVersion: NSNumber)](avcaptureancillarydataencoder/setuserinstanceuid(_:foruserudamversion:).md)
  Set the UID and Version number for the user data.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md)
  [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md) is a subclass of [`AVCaptureOutput`](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode)
- [class AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md)
  [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md) is a subclass of [`AVCaptureOutput`](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode)
- [protocol AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
- [struct AVCaptureAncillaryDataUserKey](avcaptureancillarydatauserkey.md)
  Clients may use an AVCaptureAncillaryDataUserKey to inspect the [`currentUserDefinedAncillaryData`](avcaptureancillarydataencoder/currentuserdefinedancillarydata.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureancillarydataencoder)*