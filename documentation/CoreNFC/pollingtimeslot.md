# PollingTimeSlot

**Framework**: Core NFC  
**Kind**: typealias  
**Role**: Type Alias

Constants that specify the maximum number of time slots.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: NFCFeliCaPollingTimeSlot)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: NFCFeliCaPollingTimeSlot)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: NFCFeliCaPollingTimeSlot)

## Declaration

```swift
typealias PollingTimeSlot = NFCFeliCaPollingTimeSlot
```

```c
typedef NFCFeliCaPollingTimeSlot PollingTimeSlot;
```

## Topics

### Maximum Slots
- [static var PollingTimeSlotMax1: NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot/pollingtimeslotmax1.md)
  A constant that indicates a maximum of one slot.
- [static var PollingTimeSlotMax2: NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot/pollingtimeslotmax2.md)
  A constant that indicates a maximum of two slots.
- [static var PollingTimeSlotMax4: NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot/pollingtimeslotmax4.md)
  A constant that indicates a maximum of four slots.
- [static var PollingTimeSlotMax8: NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot/pollingtimeslotmax8.md)
  A constant that indicates a maximum of eight slots.
- [static var PollingTimeSlotMax16: NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot/pollingtimeslotmax16.md)
  A constant that indicates a maximum of sixteen slots.

## See Also

### Polling
- [func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot, completionHandler: (Data, Data, (any Error)?) -> Void)](./nfcfelicatag/polling%28systemcode,requestcode,timeslot,completionhandler%29.md)
  Sends the Polling command as defined by FeliCa card specification to the tag.
- [typealias PollingRequestCode](./pollingrequestcode.md)
  Codes that specify the type of the data to request when polling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/pollingtimeslot)*