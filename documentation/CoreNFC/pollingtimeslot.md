# PollingTimeSlot

**Framework**: Core NFC  
**Kind**: typealias

Constants that specify the maximum number of time slots.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
typealias PollingTimeSlot = NFCFeliCaPollingTimeSlot
```

## Topics

### Maximum Slots
- [static var PollingTimeSlotMax1: NFCFeliCaPollingTimeSlot](nfcfelicapollingtimeslot/pollingtimeslotmax1.md)
  A constant that indicates a maximum of one slot.
- [static var PollingTimeSlotMax2: NFCFeliCaPollingTimeSlot](nfcfelicapollingtimeslot/pollingtimeslotmax2.md)
  A constant that indicates a maximum of two slots.
- [static var PollingTimeSlotMax4: NFCFeliCaPollingTimeSlot](nfcfelicapollingtimeslot/pollingtimeslotmax4.md)
  A constant that indicates a maximum of four slots.
- [static var PollingTimeSlotMax8: NFCFeliCaPollingTimeSlot](nfcfelicapollingtimeslot/pollingtimeslotmax8.md)
  A constant that indicates a maximum of eight slots.
- [static var PollingTimeSlotMax16: NFCFeliCaPollingTimeSlot](nfcfelicapollingtimeslot/pollingtimeslotmax16.md)
  A constant that indicates a maximum of sixteen slots.

## See Also

- [func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot, completionHandler: (Data, Data, (any Error)?) -> Void)](nfcfelicatag/polling(systemcode:requestcode:timeslot:completionhandler:).md)
  Sends the Polling command as defined by FeliCa card specification to the tag.
- [typealias PollingRequestCode](pollingrequestcode.md)
  Codes that specify the type of the data to request when polling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/pollingtimeslot)*