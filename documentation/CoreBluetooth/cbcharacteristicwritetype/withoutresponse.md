# CBCharacteristicWriteType.withoutResponse

**Framework**: Core Bluetooth  
**Kind**: case

Write a characteristic value, without any response from the peripheral to indicate whether the write was successful.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case withoutResponse
```

#### Discussion

You receive no notification if writing to a characteristic value fails with this write type.

## See Also

- [CBCharacteristicWriteType.withResponse](cbcharacteristicwritetype/withresponse.md)
  Write a characteristic value, with a response from the peripheral to indicate whether the write was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/withoutresponse)*