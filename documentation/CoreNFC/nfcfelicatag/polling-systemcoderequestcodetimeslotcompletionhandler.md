# polling(systemCode:requestCode:timeSlot:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Polling command as defined by FeliCa card specification to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot) async throws -> (Data, Data)
```

## See Also

- [typealias PollingRequestCode](pollingrequestcode.md)
  Codes that specify the type of the data to request when polling.
- [typealias PollingTimeSlot](pollingtimeslot.md)
  Constants that specify the maximum number of time slots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/polling(systemcode:requestcode:timeslot:completionhandler:))*