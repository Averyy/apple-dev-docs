# PollingRequestCode

**Framework**: Core NFC  
**Kind**: typealias

Codes that specify the type of the data to request when polling.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
typealias PollingRequestCode = NFCFeliCaPollingRequestCode
```

## Topics

### Request Codes
- [static var PollingRequestCodeNoRequest: NFCFeliCaPollingRequestCode](nfcfelicapollingrequestcode/pollingrequestcodenorequest.md)
  A code that indicates no request.
- [static var PollingRequestCodeSystemCode: NFCFeliCaPollingRequestCode](nfcfelicapollingrequestcode/pollingrequestcodesystemcode.md)
  A code that indicates a system code request.
- [static var PollingRequestCodeCommunicationPerformance: NFCFeliCaPollingRequestCode](nfcfelicapollingrequestcode/pollingrequestcodecommunicationperformance.md)
  A code that indicates a communication performance request.

## See Also

- [func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot, completionHandler: (Data, Data, (any Error)?) -> Void)](nfcfelicatag/polling(systemcode:requestcode:timeslot:completionhandler:).md)
  Sends the Polling command as defined by FeliCa card specification to the tag.
- [typealias PollingTimeSlot](pollingtimeslot.md)
  Constants that specify the maximum number of time slots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/pollingrequestcode)*