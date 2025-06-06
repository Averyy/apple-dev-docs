# polling(systemCode:requestCode:timeSlot:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot, resultHandler: @escaping (Result<NFCFeliCaPollingResponse, any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/polling(systemcode:requestcode:timeslot:resulthandler:))*