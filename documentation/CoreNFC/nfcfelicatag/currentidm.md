# currentIDm

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

The manufacturer identifier for the system currently selected by the reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var currentIDm: Data { get }
```

#### Discussion

The reader session updates [`currentIDm`](nfcfelicatag/currentidm.md) each time your app calls the [`polling(systemCode:requestCode:timeSlot:completionHandler:)`](nfcfelicatag/polling(systemcode:requestcode:timeslot:completionhandler:).md) method. The data contained in [`currentIDm`](nfcfelicatag/currentidm.md) is empty when the system selection fails.

## See Also

- [var currentSystemCode: Data](nfcfelicatag/currentsystemcode.md)
  The system code most recently selected by the reader session during a polling sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/currentidm)*