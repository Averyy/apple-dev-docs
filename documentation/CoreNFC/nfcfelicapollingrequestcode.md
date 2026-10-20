# NFCFeliCaPollingRequestCode

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum NFCFeliCaPollingRequestCode
```

```c
enum NFCFeliCaPollingRequestCode : NSInteger;
```

## Topics

### Enumeration Cases
- [NFCFeliCaPollingRequestCode.communicationPerformance](./nfcfelicapollingrequestcode/communicationperformance.md)
- [NFCFeliCaPollingRequestCode.noRequest](./nfcfelicapollingrequestcode/norequest.md)
- [NFCFeliCaPollingRequestCode.systemCode](./nfcfelicapollingrequestcode/systemcode.md)
### Initializers
- [init?(rawValue: Int)](./nfcfelicapollingrequestcode/init%28rawvalue%29.md)
### Type Properties
- [static var PollingRequestCodeCommunicationPerformance: NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode/pollingrequestcodecommunicationperformance.md)
  A code that indicates a communication performance request.
- [static var PollingRequestCodeNoRequest: NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode/pollingrequestcodenorequest.md)
  A code that indicates no request.
- [static var PollingRequestCodeSystemCode: NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode/pollingrequestcodesystemcode.md)
  A code that indicates a system code request.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum NFCFeliCaEncryptionId](./nfcfelicaencryptionid.md)
- [enum NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot.md)
- [struct NFCISO15693RequestFlag](./nfciso15693requestflag.md)
- [struct NFCISO15693ResponseFlag](./nfciso15693responseflag.md)
- [NFCVASResponse.ErrorCode](./nfcvasresponse/errorcode.md)
- [NFCVASCommandConfiguration.Mode](./nfcvascommandconfiguration/mode-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicapollingrequestcode)*