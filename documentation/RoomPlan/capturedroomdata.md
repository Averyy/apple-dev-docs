# CapturedRoomData

**Framework**: RoomPlan  
**Kind**: struct

An opaque object that holds the raw results of a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct CapturedRoomData
```

#### Overview

When your app completes a scan session by calling [`stop()`](roomcapturesession/stop().md), the framework provides your app with raw scan results in one of the following ways:

- The [`captureView(shouldPresent:error:)`](roomcaptureviewdelegate/captureview(shouldpresent:error:).md) callback for an app that scans rooms using the framework-provided view ([`RoomCaptureView`](roomcaptureview.md))
- The [`captureSession(_:didEndWith:error:)`](roomcapturesessiondelegate/capturesession(_:didendwith:error:).md) callback for an app that implements its own room-scanning view

With an instance of this structure, your app can:

- Process the raw data into a detailed captured room object ([`CapturedRoom`](capturedroom.md)) by creating a room builder ([`RoomBuilder`](roombuilder.md)) and calling its [`capturedRoom(from:)`](roombuilder/capturedroom(from:).md) function.
- Serialize to an encoder object, for example, to defer processing to a later date or to defer processing to another device.

## Topics

### Deserializing a prior scan
- [init(from: any Decoder) throws](capturedroomdata/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Serializing a prior scan
- [func encode(to: any Encoder) throws](capturedroomdata/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Merging multiple scans into a single structure](merging-multiple-scans-into-a-single-structure.md)
  Export a 3D model that consists of multiple rooms captured in the same physical vicinity.
- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)
  Create an AR experience that enables people to scan a building that contains multiple rooms.
- [struct CapturedRoom](capturedroom.md)
  A structure that provides the key details of a scanned room.
- [struct CapturedStructure](capturedstructure.md)
  An object that holds the results of the merger of multiple capture sessions.
- [Captured Object Attributes](captured-object-attributes.md)
  Determine details about the objects and surfaces that the framework identifies in a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroomdata)*