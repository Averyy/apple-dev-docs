# currentIDm

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, retain, readonly) NSData * currentIDm;
```

## Discussion

The reader session updates [`currentIDm`](./currentidm.md) each time your app calls the [`polling(systemCode:requestCode:timeSlot:completionHandler:)`](./polling%28systemcode,requestcode,timeslot,completionhandler%29.md) method. The data contained in [`currentIDm`](./currentidm.md) is empty when the system selection fails.

## See Also

### Getting Current Information
- [var currentSystemCode: Data](./currentsystemcode.md)
  The system code most recently selected by the reader session during a polling sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/currentidm)*