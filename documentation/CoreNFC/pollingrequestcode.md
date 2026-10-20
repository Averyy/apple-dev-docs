# PollingRequestCode

**Framework**: Core NFC  
**Kind**: typealias  
**Role**: Type Alias

Codes that specify the type of the data to request when polling.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: NFCFeliCaPollingRequestCode)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: NFCFeliCaPollingRequestCode)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: NFCFeliCaPollingRequestCode)

## Declaration

```swift
typealias PollingRequestCode = NFCFeliCaPollingRequestCode
```

```c
typedef NFCFeliCaPollingRequestCode PollingRequestCode;
```

## Topics

### Request Codes
- [static var PollingRequestCodeNoRequest: NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode/pollingrequestcodenorequest.md)
  A code that indicates no request.
- [static var PollingRequestCodeSystemCode: NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode/pollingrequestcodesystemcode.md)
  A code that indicates a system code request.
- [static var PollingRequestCodeCommunicationPerformance: NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode/pollingrequestcodecommunicationperformance.md)
  A code that indicates a communication performance request.

## See Also

### Polling
- [func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot, completionHandler: (Data, Data, (any Error)?) -> Void)](./nfcfelicatag/polling%28systemcode,requestcode,timeslot,completionhandler%29.md)
  Sends the Polling command as defined by FeliCa card specification to the tag.
- [typealias PollingTimeSlot](./pollingtimeslot.md)
  Constants that specify the maximum number of time slots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/pollingrequestcode)*