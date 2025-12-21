# init(from:)

**Framework**: RoomPlan  
**Kind**: init

Creates captured room data by deserializing the decoder of a prior scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

To serialize a scan, call [`encode(to:)`](capturedroomdata/encode(to:).md).

## Parameters

- `decoder`: An encoded captured room data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroomdata/init(from:))*