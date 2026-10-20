# init(from:)

**Framework**: RoomPlan  
**Kind**: init  
**Role**: Initializer

Creates captured room data by deserializing the decoder of a prior scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

To serialize a scan, call [`encode(to:)`](./encode%28to%29.md).

## Parameters

- `decoder`: An encoded captured room data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroomdata/init(from:))*