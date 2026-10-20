# NFCISO15693RequestFlag

**Framework**: Core NFC  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct NFCISO15693RequestFlag
```

```c
enum NFCISO15693RequestFlag : uint8_t;
```

## Topics

### Initializers
- [init(rawValue: UInt8)](./nfciso15693requestflag/init%28rawvalue%29.md)
### Type Properties
- [static var RequestFlagAddress: NFCISO15693RequestFlag](./nfciso15693requestflag/requestflagaddress.md)
  A bit mask value that turns on the address flag.
- [static var RequestFlagDualSubCarriers: NFCISO15693RequestFlag](./nfciso15693requestflag/requestflagdualsubcarriers.md)
  A bit mask value that turns on the subcarrier flag.
- [static var RequestFlagHighDataRate: NFCISO15693RequestFlag](./nfciso15693requestflag/requestflaghighdatarate.md)
  A bit mask value that turns on the high data rate flag.
- [static var RequestFlagOption: NFCISO15693RequestFlag](./nfciso15693requestflag/requestflagoption.md)
  A bit mask value that turns on the option flag.
- [static var RequestFlagProtocolExtension: NFCISO15693RequestFlag](./nfciso15693requestflag/requestflagprotocolextension.md)
  A bit mask value that turns on the protocol extension flag.
- [static var RequestFlagSelect: NFCISO15693RequestFlag](./nfciso15693requestflag/requestflagselect.md)
  A bit mask value that turns on the select flag.
- [static var address: NFCISO15693RequestFlag](./nfciso15693requestflag/address.md)
- [static var commandSpecificBit8: NFCISO15693RequestFlag](./nfciso15693requestflag/commandspecificbit8.md)
- [static var dualSubCarriers: NFCISO15693RequestFlag](./nfciso15693requestflag/dualsubcarriers.md)
- [static var highDataRate: NFCISO15693RequestFlag](./nfciso15693requestflag/highdatarate.md)
- [static var option: NFCISO15693RequestFlag](./nfciso15693requestflag/option.md)
- [static var protocolExtension: NFCISO15693RequestFlag](./nfciso15693requestflag/protocolextension.md)
- [static var select: NFCISO15693RequestFlag](./nfciso15693requestflag/select.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Enumerations
- [enum NFCFeliCaEncryptionId](./nfcfelicaencryptionid.md)
- [enum NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode.md)
- [enum NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot.md)
- [struct NFCISO15693ResponseFlag](./nfciso15693responseflag.md)
- [NFCVASResponse.ErrorCode](./nfcvasresponse/errorcode.md)
- [NFCVASCommandConfiguration.Mode](./nfcvascommandconfiguration/mode-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693requestflag)*