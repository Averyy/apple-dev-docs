# NFCVASResponse

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

An object representing the response from a single `GET VAS DATA` command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCVASResponse
```

```objc
@interface NFCVASResponse : NSObject
```

## Topics

### Getting the Response Status
- [var status: NFCVASResponse.ErrorCode](./nfcvasresponse/status.md)
  A response APDU status code.
- [typealias VASErrorCode](./vaserrorcode.md)
  Constants representing APDU status codes for a VAS response.
### Getting the VAS Data
- [var vasData: Data](./nfcvasresponse/vasdata.md)
  A data object containing the VAS data.
### Getting the Mobile Token
- [var mobileToken: Data](./nfcvasresponse/mobiletoken.md)
  A mobile token value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Receiving VAS Responses
- [func readerSession(NFCVASReaderSession, didReceive: [NFCVASResponse])](./nfcvasreadersessiondelegate/readersession%28_,didreceive%29.md)
  Tells the delegate that the reader session received a VAS response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasresponse)*