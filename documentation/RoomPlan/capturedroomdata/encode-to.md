# encode(to:)

**Framework**: RoomPlan  
**Kind**: method

Serializes captured room data to the specified encoder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

An app might serialize a [`CapturedRoomData`](capturedroomdata.md) object to defer processing to a later date or to defer processing to another device.

## Parameters

- `encoder`: An object that the captured room data serializes to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroomdata/encode(to:))*